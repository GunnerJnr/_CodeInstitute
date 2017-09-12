 
=

### LINK IN JAVASCRIPT SUPPORT TO ENABLE TINYMCE WYSIWYG EDITING

When our user clicks the *New Thread* or *New Post* buttons, we want to present
them with a nice and simple way of formatting their posts. Thus, we need to
convert each \<textarea\> tag in the html into a tinymce editor.

To do this, we need to include the JavaScript support files into our page, of
course, but we don’t want that to happen on every single page on the forum – or
else we would be making the pages’ load times slower on pages that
don’t actually use the editor.

To get past that, we’re going to use Django’s template language
command `block` to define and override a page region that will load the tinymce
library only on the pages that need it.

In our base.html, add a link to the font awesome CSS. Then add the empty block
called `head_js`:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
<head>
...
 <link rel="stylesheet" href="{% static "css/font-awesome-4.5.0/css/font-awesome.css" %}">
 
{% block head_js %}{% endblock head_js %}
...
</head>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

On our pages that do the editing, we can now include an override for that to
include our initialisation code. Let’s create a new template
called *thread_form.html* and add the code below:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
{% extends "base.html" %}
{% load bootstrap_tags %}
{% load staticfiles %}
 
{% block head_js %}
   <script src="{% static 'js/tinymce/tinymce.min.js' %}"></script>
   <script>
       tinyMCE.init({mode: "textareas", theme: 'modern', plugins: 'paste'})
   </script>
{% endblock %}
 
 
{% block content %}
   <section>
       <div class="col-md-9">
           <form method="post" action="{% url 'new_thread' subject.id %}">
               {% csrf_token %}
               {{ thread_form | as_bootstrap }}
               <hr>
               {{ post_form | as_bootstrap }}
 
               <div class="form-group">
                   <button type="submit" class="btn-primary"> Post New Thread</button>
               </div>
           </form>
       </div>
   </section>
{% endblock %}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When the page is rendered, all \<textarea\> sections are now rendered as WYSIWYG
editors.  


![](http://codeinstitute.wpengine.com/wp-content/uploads/2016/01/1452537277_image3.png)

 

### ADD NEW POSTS TO THREADS

After creating a thread and a single post, we can display it using the normal
methods we would use to fetch any data for a standard view displaying objects.

Now we will add the functionality referred to in *thread_item.html*. Remember
the *thread* view being referenced in the code:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
<td>
         <a href="{% url 'thread' thread.id %}"><h4>{{ thread.name }}</h4></a>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

So let’s create that view now and then we’ll create its associated url pattern
and template. Add the *thread* view to *threads.views.py* as per below:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
...
from threads.models import Subject, Post, Thread
...
 
def thread(request, thread_id):
    thread_ = get_object_or_404(Thread, pk=thread_id)
    args = {'thread': thread_}
    args.update(csrf(request))
    return render(request, 'forum/thread.html', args)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Add the url pattern:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
url(r'^thread/(?P<thread_id>\d+)/$', forum_views.thread, name='thread'),
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Then create a template called *thread.html* as per below:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
{% extends "base.html" %}
{% load thread_extras %}
{% load staticfiles %}
{% block content %}
 
 <div class="row header">
 
   <div class="container">
     <h2>{{ thread.name }}</h2>
     <div class="col-md-12">
         <table class="table">
             <tbody>
             <tr>
                 <th>
                   CREATED
                 </th>
                 <th>OWNER</th>
                 <th>LAST POST</th>
             </tr>
             <tr>
                 <td>
                   <time datetime="{{ thread.created_at }}">
                    {{ thread.created_at|started_time }}
                   </time>
                 </td>
                 <td>{{ thread.user.username }}</td>
                 <td>{% last_posted_user_name thread %}</td>
             </tr>
           </tbody>
         </table>
     </div>
     {% if user.is_authenticated %}
       <p>
         <a href="{% url 'new_post' thread.id %}" class="btn btn-primary">New post</a>
       </p>
     {% endif %}
   </div>
 </div>
 <div class="container">
   {% for post in thread.posts.all %}
     {% include "forum/post.html" %}
   {% endfor %}
 </div>
{% endblock %}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Again we have loaded the thread_extras file and are referencing a custom filters
called `started_time` and `last_posted_user_name`.

Let’s update our thread_extras.py file to include these filters:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@register.filter
def started_time(created_at):
   return arrow.get(created_at).humanize()
 
 
@register.simple_tag
def last_posted_user_name(thread):
    last_post = thread.posts.all().order_by('created_at').last()
    return last_post.user.username
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create a new template in the forums template directory called *post.html*:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
{% load staticfiles %}
{% load emoticons_tags %}
<section class="row comment col-md-9">
 <div class="col-md-3 comment-profile">
   <p><img src="{% static 'images/user.png' %}" /></p>
   <p>{{ post.user.username }}</p>
   <p>{{ post.user.posts.count }} POSTS</p>
 </div>
 <div class="col-md-9 ">
   <div class="comment-content">
     {% autoescape off %}
       {{ post.comment|emoticons }}
     {% endautoescape %}
   </div>
   {% include "forum/comment_details.html" %}
 </div>
 
</section>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Notice that in the above code, we include the use of emoticons in our comments.
We also reference a `comment_details` template.  We’ll come back to this later.

When it comes to adding a new post, aside from adding in the TinyMCE editor, our
post creation view and template should now start looking like familiar
territory. Here’s our *new_post* view in *threads/views.py*:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@login_required
def new_post(request, thread_id):
    thread = get_object_or_404(Thread, pk=thread_id)
 
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(False)
            post.thread = thread
            post.user = request.user
            post.save()
 
            messages.success(request, "Your post has been added to the thread!")
 
            return redirect(reverse('thread', args={thread.pk}))
    else:
        form = PostForm()
 
    args = {
        'form' : form,
        'form_action': reverse('new_post', args={thread.id}),
        'button_text': 'Update Post'
    }
    args.update(csrf(request))
 
    return render(request, 'forum/post_form.html', args)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As you can see, it’s more of the same pattern you’ve seen in other views that
create objects from model forms. The only thing to note of course is that here
we:

1.  Save the form with the False setting to stop Django committing the data to
    the database right away. This would cause a database error, as we need to
    set the thread and user first and then save the post.

2.   Set the thread and user fields for our post.

3.  And finally, save the post object complete with all related data.

Here’s our url pattern for the view:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
url(r'^post/new/(?P<thread_id>\d+)/$', forum_views.new_post, name='new_post'),
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Here what our *post_form.html* template looks like:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
{% extends 'base.html' %}
{% load bootstrap_tags %}
{% load staticfiles %}
{% block head_js %}
<script src="{% static 'js/tinymce/tinymce.min.js' %}"></script>
<script type="text/javascript">
 tinyMCE.init({
   mode: "textareas",
   theme: "modern",
   plugins: "paste",
});
</script>
{% endblock %}
{% block content %}
 <section>
   <div class="col-md-9">
     <form method="post" action="{{ form_action }}">
       {% csrf_token %}
       {{ form|as_bootstrap }}
       <div class="form-group">
         <button type="submit" class="btn btn-primary">{{button_text}}</button>
       </div>
     </form>
   </div>
 </section>
{% endblock %}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Again, this is all starting to look very similar to the forms we’ve made in the
past – so we’re in familiar territory.
