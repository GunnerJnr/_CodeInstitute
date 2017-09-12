### SHOWING OUR SUBJECTS

When our user visits the forum section of our site, we want to initially show
them a list of subjects that the threads are contained in.

 

### NOTE

  
Subjects will be created ONLY in the site admin pages as only the site admin
should be able to specify what subjects are available to be discussed on your
forum. Once you’ve create the model and run your migrations later you should
login to the admin and create a few subjects to play around with.

 

Let’s write our admin pages now by opening up *threads/admin.py*:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.contrib import admin
from .models import Subject, Thread, Post
 
admin.site.register(Subject)
admin.site.register(Thread)
admin.site.register(Post)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

To display the subjects, we simply pull the all subjects from the database and
pass them to our view. Here’s our code to take care of the task of controlling
the saving process:

Add a new view called *forum* to *threads.views.py*:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.shortcuts import render
from threads.models import Subject
 
def forum(request):
   return render(request, 'forum/forum.html', {'subjects': Subject.objects.all()})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Then we’ll create new folder in folder in our templates directory
called *forum* then create a template called *forum.html* that
extends *base.html*.

And in our template, we show each subject with a link to the ‘threads’ view
which will display our threads within that subject:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
{% extends "base.html" %}
{% load thread_extras %}
{% block content %}
   {% load bootstrap_tags %}
   {% for subject in subjects %}
       <section class="subject">
           <h2><a href="{% url "threads" subject.id %}">{{ subject.name }}</a></h2>
           <p>
               <a href="{% url "threads" subject.id %}">
                   {% autoescape off %}{{ subject.description }}{% endautoescape %}
               </a>
           </p>
           <table>
               <tr>
                   <th>THREADS</th>
                   <th> POSTS</th>
               </tr>
               <tr>
                   <td>{{ subject.threads.count }}</td>
                   <td>{{ subject|get_total_subject_posts }}</td>
               </tr>
           </table>
       </section>
   {% endfor %}
{% endblock %}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

The above template refers to some functionality that is not yet in place, such
as:

-   `thread_extras` – contains custom template tag functionality

-   `url threads` – used to navigate to threads associated with a subject

Let’s put this functionality in place now.

 

First create a view in *threads/views.py* that maps to the thread url. Notice
that this view takes in a `subject_id` as a parameter:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.shortcuts import render, get_object_or_404
...
 
 
def threads(request, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id)
    return render(request, 'forum/threads.html', {'subject': subject})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Now we create a url pattern to bind to the threads view as well as the url for
our forum view:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
...
from threads import views as forum_views
 
urlpatterns = [
    ...
    url(r'^forum/$', forum_views.forum),
    url(r'^threads/(?P<subject_id>\d+)/$', forum_views.threads, name='threads'),
]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Now let’s add a link to the nav bar in our *base.html* so we can see the forum
subjects:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
...
<li><a href="/forum/">Forum</a></li>
...
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Next we need to create a template to bind our threads view to. Create a new
template called *threads.html* and add the code shown below. And in our template
we render all, if any, of the threads for that subject:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
{% extends "base.html" %}
{% load thread_extras %}
{% block content %}
 <div class="row header">
   <div class="jumbotron"><h1>{{ subject.name }}</h1></div>
 </div>
 <div class="col-md-12">
   {% if user.is_authenticated %}
     <p>
       <a href="{% url 'new_thread' subject.id %}" class="btn btn-primary">New Thread</a>
     </p>
   {% endif %}
   {% for thread in subject.threads.all %}
     {% include "forum/thread_item.html" %}
   {% endfor %}
 </div>
{% endblock %}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

We’re not quite there yet. As you can see, there are a chain of dependencies
that we need to put in place before we can display our forum subjects and any
associated thread topics.  In the above file, we refer to another view
called *new_thread*. Let’s put this in place now.

First, we create a new view called *new_thread* in *threads.views.py*. Because
there is a danger of us going down a rabbit-hole of complexity at this point,
let’s put the bare skeleton of our view in place for now. This view allows
logged in users to create a new thread.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.shortcuts import render, get_object_or_404
from models import Subject, Thread, Post
from django.shortcuts import redirect
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.template.context_processors import csrf
 
 
@login_required
def new_thread(request, subject_id):
    pass
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Add the url pattern that we use bind to the *new_thread* view as per below:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
url(r'^new_thread/(?P<subject_id>\d+)/$',  forum_views.new_thread, name='new_thread'),
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

We also use the template ‘include’ tag in *forum/threads.html*, to include a
template called *thread_item.html* to show how our individual thread names
should be rendered on this page. The template looks like this:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
<section class="thread">
 <header>
   <table>
     <tr>
       <td>
         <a href="{% url 'thread' thread.id %}"><h4>{{ thread.name }}</h4></a>
       </td>
     </tr>
   </table>
 
 </header>
</section>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Notice in the code above that we refer to yet another view called *thread*.
 We’ll put that in place in a little while.

Even without the *thread* view in place, our code will still throw an exception
when run. This is because we don’t have the thread_extras templatetags file in
place yet. Why do we need this again? If you look back at our forum.html
template, you’ll see a reference to a custom template tag
called `get_total_subject_posts`.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
<td>{{ subject.threads.count }}</td>
<td>{{ subject|get_total_subject_posts }}</td>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

We need to put the code for this tag in place.

So the first thing we do is create a new directory called *templatetags* within
our threads app. Inside the directory, we add two files as shown below.

 

![](http://codeinstitute.wpengine.com/wp-content/uploads/2016/01/1452537277_image6.png)

  
Add the following code to *thread_extras.py*. This filter function will return a
count of all the posts associated with a particular thread, which in turn is
associated with a subject.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import arrow
from django import template
from django.core.urlresolvers import reverse
 
register = template.Library()
 
@register.filter
def get_total_subject_posts(subject):
   total_posts = 0
   for thread in subject.threads.all():
       total_posts += thread.posts.count()
   return total_posts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

So for every item in the *threads.html* template, we include this template that
describes how it will be displayed.

![](http://codeinstitute.wpengine.com/wp-content/uploads/2016/01/1452537277_image7.png)

  
If the user is logged in, we allow them to create a new thread. So let’s now
look at what should happen when the user clicks that link.

![](http://codeinstitute.wpengine.com/wp-content/uploads/2016/01/1452537277_image8.png)
