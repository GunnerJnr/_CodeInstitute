### SETUP THE ADMIN PAGE WITH POSTS

Ok, so far so good.  We’ll get to the views and templates later, but for now
we’ll create and edit some posts via the Admin page.  
Have you added a **superuser** to get admin access yet? If not, do it now.

### REGISTER THE POST MODEL

1.  Go to **admin.py** in our blog app and register the **Post** model. Don’t
    forget the dot (**.**) on the models import.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.contrib import admin
from .models import Post
 
admin.site.register(Post)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1.  Fire up the server and go to the admin page. You should see
    the **Post** model added to the admin screen. Add some new blog posts.
    Notice that you need a registered user as author in order to save the post.
    Also, notice that you can delay publishing a post once it is written. Not a
    bad option when writing a particularly virulent response to some injustice
    or other and you might want to have a cooling off period…

 

![](http://codeinstitute.wpengine.com/wp-content/uploads/2015/12/1449505716_image3.png)

 

 **COMPLETED CODE**  
The code for this lesson can be found
at <https://github.com/Code-Institute-Org/full_stack_solutions/tree/master/Stream-Three/Unit05-Django_Blog_Part1>

 

### SUMMARY

In this lesson, we’ve learned that:

-   All blog entries are stored to and accessed from an SQLite database through
    the use of models.

-   Django provides a file called **tests.py** out of the box for writing unit
    tests.  

-   Blog posts can be added from the Admin interface.
