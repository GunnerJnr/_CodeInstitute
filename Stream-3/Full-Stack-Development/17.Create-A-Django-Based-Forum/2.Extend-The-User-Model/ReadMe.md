###  

Extend the User Model to Add Threads and Posts to the User’s Profile
====================================================================

##### In this unit the students will learn how to extend Django's default user model and how they can apply threads and post to a users profile

 

### EXTEND THE USER MODEL TO ADD THREADS AND POSTS TO THE USER’S PROFILE

The next stage is to begin developing our forum. In this process, we’ll be
extending our existing account.User model, so let’s start by working out what
models we’ll need for our forum.

Most forums have a set of subjects and then store threads under each of the
subjects. In addition, while creating each thread, a post is created alongside
it. After that, each thread will also need to track its own posts. And finally,
each thread and each post must remember who created them. This may seem a fairly
complex setup, but you can be sure that this is what Django was build to
simplify!

We’ll begin by creating a new app in our project called ‘threads’ to hold our
forum’s information. Within that app, we’re going to create some models that
will have our account.User model as a ForeignKey reference. By making this
reference back to the accounts.User model, we’re actually extending what that
model has.

As an example, we will add a Thread model that will reference our accounts.User
model as its ‘user’ field. But in our accounts.User model this will become
accessible as the ‘user.threads’ field in the process of creating the
relationship. So even though we’re not editing the accounts.User model directly,
we are modifying its relationships by specifying them in our new models.

### A WALK THROUGH

Create a new app called **‘threads’** and configure Django to use it.

Now we can begin making our models in the **threads/models.py file**. Let’s
start with our Subject model:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField
from django.conf import settings
 
 
class Subject(models.Model):
 
    name = models.CharField(max_length=255)
    description = HTMLField()
 
    def __unicode__(self):
        return self.name
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Here we add two fields: `name` and `description`.

`Description` is a new field that comes packaged with django-tinymce. It enables
our field to render the WYSIWYG editor in our admin.

As we won’t be allowing our users to access these records, we’ll only allow
staff to edit the subject areas that users can start threads in.

Now let’s add a Thread model in the **threads/models.py**:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.utils import timezone
...
class Thread(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='threads')
    subject = models.ForeignKey(Subject, related_name='threads')
    created_at = models.DateTimeField(default=timezone.now)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We’re now beginning to add in the relationships to each model and as you can
see, it is as simple as adding in a `ForeignKey` field that will establish a
one-to-many relationship with both our user and our threads subject category.

 

### NOTE

When choosing what relationship to establish, it is helpful to talk out loud
about what the relationship actually is. You could say *my thread is owned by
one user, but there is more than one user. The thread also belongs to one
subject category, but there is more than one subject.* 

In that way, we know that it’s a one-to-many.

 

Finally, we’re going to record the time the posts and threads are created, so we
can display it on the forum. To do this, we add in the
DateTimeField `created_at`.

Next, let’s take a look at our Post model in the threads/models.py:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Post(models.Model):
    thread = models.ForeignKey(Thread, related_name='posts')
    comment = HTMLField(blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='posts')
    created_at = models.DateTimeField(default=timezone.now)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Again we’re using the `ForeignKey` field to connect our many posts to one single
thread, and to link back to the user who created the post.

We reuse the `HTMLField` to enable this field to use **tinymce** on the forum
pages too.

After defining these, we need to run the **python manage.py
makemigrations** command to create our migrations, which will specify how to
modify the database to work with our models.

Once that’s done, we’re safe to run our migrate command (**python manage.py
migrate**).
