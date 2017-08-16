### CREATE OUR MODEL

Often it can be useful to get your data in place early in a project, especially
one like a blog where almost all the page content is dynamically generated and
accessed from a database. So in the case of our blog_prj project, we’ll get our
models in place first and once we are happy with the data, we’ll then create our
views and templates. Let’s create a model class called **Post** that inherits
from **Model**. The class will have these attributes:

-   Post title

-   Creation date

-   Published date

-   Post content

-   Author

Add the code below to **models.py** in your blog app:

 

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.db import models
from django.utils import timezone
 
 
class Post(models.Model):
    """
    Here we'll define our Post model
    """
 
    # author is linked to a registered
    # user, via the User model in the auth app. 
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)
 
    def publish(self):
        self.published_date = timezone.now()
        self.save()
 
    def __unicode__(self):
        return self.title
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Let’s take a closer look at what we just did.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # author is linked to a registered
    # user, via the User model in the auth app. 
    author = models.ForeignKey('auth.User')
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Our blog does not allow anonymous posts, so we link a new blog post to a
registered user, such that we’ll get the author details from the User model.
Behind the scenes, this means that our post table will now have a foreign key
relationship with the **auth_user** table, but when using Django’s model
abstraction like this (rather than working directly with SQL), we can generally
disregard the tables and think just about the model relations.

The post title and content attributes are standard Charfield types with a
restriction on the title length.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    title = models.CharField(max_length=200)
    content = models.TextField()
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We can also use **auto_now_add=True** to identify when the post was created.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    created_date = models.DateTimeField(auto_now_add=True)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We may choose not to publish a blog post immediately. So, our **published
date** will initially be set to **blank** and **null**.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    published_date = models.DateTimeField(blank=True, null=True)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

But when we do decide to publish the blog entry, our **publish** function can be
called to update the database.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def publish(self):
        self.published_date = timezone.now()
        self.save()
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Finally, we need to identify our blog entries on our admin page. We’ll use the
title as the identifier for each blog post instance.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __unicode__(self):
        return self.title
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now, run the **makemigrations** and **migrate** commands to update your
database.
