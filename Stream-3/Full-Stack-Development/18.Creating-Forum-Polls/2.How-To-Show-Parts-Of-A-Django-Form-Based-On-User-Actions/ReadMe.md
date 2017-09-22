### HOW TO SHOW PARTS OF A DJANGO FORM BASED ON THE USER’S ACTIONS

We started by defining our models, but when we come to actually displaying the
forms, we have a special circumstance that we need to take care of.

When we want a normal thread, we don’t want to show the other fields in the
form, and we also want to avoid creating a Poll object or any of its dependent
classes if we don’t need any. We should only show the relevant fields when we
actually want to create a poll.

To handle this situation, we can add in an extra field in our `ModelForm` for
our `ThreadForm` object in threads/forms.py:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class ThreadForm(forms.ModelForm):
    name = forms.CharField(label="Thread name")
    is_a_poll = forms.BooleanField(label="Include a poll?", required=False)
 
    class Meta:
        model = Thread
        fields = ['name']
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   
We called the field `is_a_poll`, but we’ve changed the label to make it more
user friendly. That is not a required field. We want to see it on the form, but
we don’t care if it’s not included, as it will be missing from our request.POST
if it’s not checked.

That way, we avoid any validation errors that might stop the process when all we
want is to be able to tell whether or not is a poll!

Next, we have our `Poll` and `PollSubject` forms. Let’s create them in
polls/forms.py:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django import forms
from models import Poll, PollSubject
class PollForm(forms.ModelForm):
    question = forms.CharField(label="What is your poll about?")
    class Meta:
        model = Poll
        fields = ['question']
 
class PollSubjectForm(forms.ModelForm):
    name = forms.CharField(label="Poll subject name", required=True)
 
    def __init__(self, *args, **kwargs):
        super(PollSubjectForm, self).__init__(*args, **kwargs)
 
        self.empty_permitted = False
 
    class Meta:
        model = PollSubject
        fields = ['name']
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

These are pretty standard, except for the renaming of the labels to make them
fit the context of entering the information along with your new thread. As well
as this, we override `__init__` so that the ’empty_permitted’ validation option
is set to False. Formsets by default allow empty fields, but we don’t want that
in our case.

The interesting part comes when we talk about something we mentioned earlier. We
want THREE subjects!

The first thought you might have in creating these is to create three different
forms, pass the `request.POST`, and process them one at a time:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
subject1 = PollSubjectForm(request.POST)
subject2 = PollSubjectForm(request.POST)
subject3 = PollSubjectForm(request.POST)
 
if subject1.is_valid() and subject2.is_valid() and subject3.is_valid():
   do_somthing()
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To be fair, you wouldn’t be wrong for thinking this way!

However, those nice coders over at the Django project thought of an even better
way to solve the problem using something called **formsets**.

With a formset, you can take one form class and tell how many you want using its
‘extra’ argument.

Modify the new `new_thread` view in *threads/views.py* to give us the option of
creating a poll when creating a new thread.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
...
from django.forms import formset_factory
from polls.forms import PollSubjectForm, PollForm
 
@login_required
def new_thread(request, subject_id):
   subject = get_object_or_404(Subject, pk=subject_id)
   poll_subject_formset_class = formset_factory(PollSubjectForm, extra=3)
   if request.method == "POST":
       thread_form = ThreadForm(request.POST)
       post_form = PostForm(request.POST)
       poll_form = PollForm(request.POST)
       poll_subject_formset = poll_subject_formset_class(request.POST)
       if (thread_form.is_valid() and
                post_form.is_valid() and
                poll_form.is_valid() and
                poll_subject_formset.is_valid()):
           thread = thread_form.save(False)
           thread.subject = subject
           thread.user = request.user
           thread.save()
 
           post = post_form.save(False)
           post.user = request.user
           post.thread = thread
           post.save()
 
           poll = poll_form.save(False)
           poll.thread = thread
           poll.save()
 
           for subject_form in poll_subject_formset:
               subject = subject_form.save(False)
               subject.poll = poll
               subject.save()
 
           messages.success(request, "You have created a new thread!")
 
           return redirect(reverse('thread', args={thread.pk}))
 
   else:
       thread_form = ThreadForm()
       post_form = PostForm()
       poll_form = PollForm()
       poll_subject_formset = poll_subject_formset_class()
 
   args = {
        'thread_form': thread_form,
        'post_form': post_form,
        'subject': subject,
        'poll_form': poll_form,
        'poll_subject_formset': poll_subject_formset,
   }
 
   args.update(csrf(request))
 
       return render(request, 'forum/thread_form.html', args)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Then loop through them when rendering.

Modify the *forum/thread_form.html* template to include poll structure:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
{% extends "base.html" %}
{% load bootstrap_tags %}
{% load staticfiles %}
 
{% block head_js %}
   <script type="text/javascript" src="{% static 'js/tinymce/tinymce.min.js' %}"></script>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
   <script type="application/javascript">
       tinyMCE.init({mode: "textareas", theme: 'modern', plugins: 'paste'})
 
   </script>
{% endblock %}
 
 
{% block content %}
   <section>
       <div class="col-md-9">
           <form method="post" action="{% url 'new_thread' subject.id %}">
               {% csrf_token %}
               <div class="form-group">
                   {{ thread_form | as_bootstrap }}
                   <hr>
                   {{ post_form | as_bootstrap }}
               </div>
               <div id="poll_form" class="form-group">
                   {{ poll_form|as_bootstrap }}
                   {{ poll_subject_formset.management_form }}
                   {% for poll_subject_form in poll_subject_formset %}
                       {{ poll_subject_form|as_bootstrap }}
                   {% endfor %}
               </div>
               <div class="form-group">
                   <button type="submit" class="btn-primary"> Post New Thread</button>
               </div>
           </form>
       </div>
   </section>
  <!-- JQuery Stuff to go in here -->
{% endblock %}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

So when you get them back in the `request.POST`, you simply use
the `PollSubjectFormset` like you’d use a normal form:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
poll_form = PollForm(request.POST)
poll_subject_formset = PollSubjectFormset(request.POST)
…
if thread_form.is_valid() and post_form.is_valid() \
                and poll_form.is_valid() and poll_subject_formset.is_valid():
...
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When calling the `is_valid`, the formset will validate all your forms in one go,
so you can effectively treat them like they are one form!

When it’s time to pull out the values from each form, you simply loop through
each one as you did when rendering:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
for subject_form in poll_subject_formset:
    subject = subject_form.save(False)
    subject.poll = poll
    subject.save()
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### HIDING AND SHOWING NEEDED FORM PARTS

Now that we know how the form will be rendered, we also know that all these
fields will be visible, so we need to hide them.

Add the code below to *thread_form.html* (insert where we added the JQuery
comment):

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
<script>
    function showOrHidePollForm() {
        if ($('#id_is_a_poll').is(':checked')) {
            $('#poll_form').show();
        } else {
            $('#poll_form').hide();
        }
    }
 
    $(document).ready(showOrHidePollForm);
    $('#id_is_a_poll').change(showOrHidePollForm);
</script>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Here, we first check to see if our checkbox `is_a_poll` is checked already. This
is because we might have already submitted the form, but the validation has
failed. If that’s true, we need to leave that part of the form visible.

If it’s not, then we should act like this is the first time the form has been
rendered and hide these fields.

Then, we watch for the click event to be fired on our `is_a_poll` checkbox and
show or hide the fields, depending on its state.

When we submit the form, we also need to alter the save behaviour depending on
whether or not a poll has been included. In the ‘new_thread’ view in
‘threads/views.py’ there is an if statement that checks if the forms are valid
and then saves both the new thread/post and the poll.

We want to amend that so that the thread/post is always saved, but we only
attempt to save a poll if one was included.

Use the following if statement to determine if the thread includes a poll, and
amend the existing code. You’ll need to figure out how to do this.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if 'is_a_poll' in request.POST:
    # save our poll information!
else:
    # save our thread without a poll
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

So depending on our checkbox’s state, we can control how much work is done in
saving our thread.
