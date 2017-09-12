Collect Information From Multiple Forms in One Go
=================================================

##### In this unit the students will learn how they can use Django to collect data from multiple HTML forms at once

 

### COLLECT INFORMATION FROM MULTIPLE FORMS IN ONE GO

As a reminder :

-   You must be an admin to create a subject via the admin screen

-   A subject can have zero or more topic threads associated with it

-   A thread can be commented on in the form of zero or more posts

-   You must be logged in to create a thread or a post

So far, you’ve seen how to use forms to populate records and insert them into
one record. Now we’ve got an unusual situation where we’re trying to collect a
thread and post all in one page.

No problem! Django makes this task simple too. All we need to do is pass
the `request.POST` into both of our forms, and Django will let us validate and
save both as normal.

However, we have an added layer of complexity here because we need to save the
thread before we save our post. Our post cannot save unless we have a thread to
assign to it.

Let’s return to our *new_thread* view. Here’s our code to take care of the task
of controlling the saving process:  

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 
...
from .forms import ThreadForm, PostForm
 
@login_required
def new_thread(request, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id)
    if request.method == "POST":
        thread_form = ThreadForm(request.POST)
        post_form = PostForm(request.POST)
        if thread_form.is_valid() and post_form.is_valid():
            thread = thread_form.save(False)
            thread.subject = subject
            thread.user = request.user
            thread.save()
 
            post = post_form.save(False)
            post.user = request.user
            post.thread = thread
            post.save()
 
            messages.success(request, "Your have create a new thread!")
 
            return redirect(reverse('thread', args={thread.pk}))
    else:
        thread_form = ThreadForm()
        post_form = PostForm()
 
    args = {
        'thread_form' : thread_form,
        'post_form' : post_form,
        'subject' : subject,
    }
    args.update(csrf(request))
 
    return render(request, 'forum/thread_form.html', args)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In this view, we refer to two forms:

1.  ThreadForm

2.  PostForm

As you can see, we can collect all the needed form information and then
use `is_valid()` for each of those forms, all in the same if statement.

When it’s time to save the thread, we don’t have any information about the
current user in our form, so we pass `False` into our save method, which avoids
committing the data to the database. Instead, it returns a memory-only version
of the model. We can then assign the user from the `request.user` that’s being
stored, since the user logged in and saved.

Now that we have a saved version of the thread, we can again create a
memory-only version of the Post model and assign our user and thread just before
we save it.

Another interesting thing is that this is possibly the first time we’ve used
reverse to pass to a view that’s expecting arguments. We do this by adding in
the extra ‘args’ dict to supply the needed thread id.

Let’s now create our ThreadForm and PostForm forms. Create a new *forms.py* file
within our *threads* app  and add the two forms as shown below:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django import forms
from .models import Thread, Post
 
 
class ThreadForm(forms.ModelForm):
   class Meta:
       model = Thread
       fields = ['name']
 
 
class PostForm(forms.ModelForm):
   class Meta:
       model = Post
       fields = ['comment']
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
