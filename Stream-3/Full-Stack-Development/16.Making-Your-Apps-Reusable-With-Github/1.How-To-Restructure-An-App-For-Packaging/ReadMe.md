How to Restructure an App for Packaging
=======================================

##### In this unit the students will learn how to restructure their Django app to make it reuseable

 

### HOW TO RESTRUCTURE AN APP FOR PACKAGING

Let’s say we have decided that we’re very happy with one of the apps we’ve built
(in this example our blog app) and we’d want to split it off and repackage it as
a reusable component to be later reused it in several different projects.

So first off, we need to look at the structure of our existing app and make sure
that its various parts are ‘decoupled’ from the existing project.

![](http://codeinstitute.wpengine.com/wp-content/uploads/2016/01/1452278888_image2.png)

  
We have a blog folder and various other folders. We need to take the most
important files and folders and place them into the blog folder, so that when we
package this app, they will be included in the package and installed along with
our code.

First, let’s make some changes to our code.

In order for our Post model to retain its relationship with the User model
across different Django projects, we’ll need to use
the `AUTH_USER_MODEL` setting (it will point to the default User model, unless
overridden in a specific project). So in your blog/models.py make sure you have
the following code:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
...
from django.conf import settings
 
 
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    ...
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once this is done, we’ll make a slight change to blog/urls.py so it looks like
this:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.conf.urls import url
import views
 
urlpatterns = [
    url(r'^$', views.post_list, name="post_list"),
    url(r'^/$', views.post_list, name="post_list"),
    url(r'^/stuff/$', views.post_list, name="post_list"),
    url(r'^(?P<id>\d+)/$', views.post_detail),
    url(r'^post/$', views.new_post, name='new_post'),
]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All we’ve done here is remove the ‘blog/’ at the beginning of each URL. The
reason we’ve done this is because later we’ll be importing these URLs into an
existing project and we’ll add the ‘blog/’ prefix there instead.

   
Django apps are essentially the same as Python packages, so when they are
installed, they will be installed in your Python install folders under
‘site-packages’, which is found in your *virtualenv* folder under
‘lib/Python2.7/site-packages’.

We need to copy the templates for our blog into a templates folder inside of our
blog folder, so that we have ‘blog/templates/blog’. This would match the
code’s references to our templates in our ‘blog/views.py’:

`return render(request, "blog/postdetail.html",{'post': post})`

Also, we have some css that is currently in the ‘static/css/blog.css’ that we
would like to include, so we need to create a ‘static/css’ folder inside our
blog app folder too, and copy our css file in there.

![](http://codeinstitute.wpengine.com/wp-content/uploads/2016/01/1452278888_image3.png)
