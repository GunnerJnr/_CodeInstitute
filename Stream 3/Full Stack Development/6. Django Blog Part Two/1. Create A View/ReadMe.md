### CREATE A VIEW

Let’s begin wiring out model up to the view.

1.  Add a new view called **post_list** in views.py. Don’t forget to import the
    model!

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.shortcuts import render
from django.utils import timezone
from .models import Post
 
 
def post_list(request):
    """
    Create a view that will return a
    list of Posts that were published prior to'now'
    and render them to the 'blogposts.html' template
    """
    posts = Post.objects.filter(published_date__lte=timezone.now()
        ).order_by('-published_date')
    return render(request, "blogposts.html", {'posts': posts})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### WHAT’S NEW IN THIS CODE?

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    posts = Post.objects.filter(published_date__lte=timezone.now()
        ).order_by('-published_date')
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Django allows us to append strings to table fields that act as boolean
operators.

In our case, we are appending **” \__lte”**, which stands for
“less-than-or-equal-to” (**\<=**) to our published_date field. This means that
the **QuerySet** returned will only return blogs published up to now.

This can be useful for blogs with a published date in the future to be only made
available when the time comes. The blogs are also ordered by **published_date**.
And by default, it will arrange the latest date first. The negative sign in
front of **published_date** indicates descending order. Ascending order is
otherwise implied.

 

### DECOUPLE THE CALL TO THE VIEW

Until now, we have been calling the view function name directly at the project
level in our projects **urls.py** file. In the spirit of good object oriented
practices however, this is not the best approach.

An app should really be responsible for the urls and the view names. The project
should really only know that the app exists and that the app makes use of urls.
By moving the implementation details of how the url call is constructed – i.e.,
the regular expression and the view name – to the app, we can make changes to
these values within the app without affecting the project.

1.  Add a new file called **urls.py** inside the **blog** directory.

2.  Add a similar structure to the file that’s contained in the urls file at the
    project level.

3.  Add a reference to the above file in the urls file located in the project
    root (**blog_prj.urls.py**). Our addition is on **line 7**. Notice that we
    use an include function to find the urls file in the blog app – just like
    the admin is accessed.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.conf.urls import include, url
from django.contrib import admin
 
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('blog.urls'))
]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

None of code we just created up to now will work yet because we haven’t created
our **blogposts.html** template that the **post_list** view is looking for.
Let’s do that now.
