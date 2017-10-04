###  

Getting Started With Django-Rest-Framework
==========================================

##### In this unit the students will learn how to get started with the Django REST Framework

 

Let’s go ahead and start a new **Django** project in **Pycharm**. Call the
project and the virtualenv **django_todo** and create a new Django
app called **todo**.

 

Next we need to install **djangorestframework**.

![](http://codeinstitute.wpengine.com/wp-content/uploads/2016/11/1479225809_image2.png)

  
Next we’ll add it to our **INSTALLED_APPS** setting in **settings.py** file
located in **django_todo** directory.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'todo'
]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Don’t forget to add our **todo** app the **INSTALLED_APPS** while we’re there!
Now that we have those in place, we’ll go ahead and get to work on
our **Todo** model.

 

Let’s open up **models.py** in our **todo** app and add in the following:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
 
# Two-sequence containing the different possible
# states of a todo item
STATUS_CHOICES = (
    ('1', 'Todo'),
    ('2', 'Doing'),
    ('3', 'Done')
)

 
class Todo(models.Model):
     """
    Todo model.
 
    Contains the `title`, `description`, `status` and `updated` fields
    for a Todo item
    """
 
    title = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=255, null=False)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    updated = models.DateTimeField(default=timezone.now)
 
    def __unicode__(self):
        return self.title
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Now we have our model in place:

-   **STATUS_CHOICES** is a nested tuple.

-   Inside the **STATUS_CHOICES** tuple, we have three more tuples. Think of
    these as **key/value** pairs.

-   On **line 25** we have the **status** field. This is almost like a
    normal **CharField**, except we can give it the **choices** parameter.

 

If we were to render this field as a form, it would render as
a **select** field, just like this:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
<select>
  <option value="1">Todo</option>
  <option value="2">Doing</option>
  <option value="3">Done</option>
</select>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When we save this in the model, it will store the **key**. So if we wanted to
create a new item that had a **status** of **Todo**, we would need to store
the **key** associated with that **value**, which is **1**.

When we bind this to a template, it will use that **key** as a lookup – so it
will display **Todo**.

We also have the **updated** field on **line 26**. This is
a **DateTimeField**, and we use timezone.now to update the field every time the
a model instance is saved (i.e. everytime we call the **.save()**method.)

 

Let’s see what we’ve got so far. First, we’ll update the **admin.py** file in
our **todo** app:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.contrib import admin
from todo.models import Todo
 
admin.site.register(Todo)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now we need to activate our virtualenv so we can run our migrations and create a
superuser – and then we’ll run the server!

 

We’ll execute these commands in **Pycharm’s** **Terminal**:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
<path_to_env>\Scripts\activate
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once that’s all done, just run the server by clicking on the **Run** button
in **Pycharm**.

 

Now head over to **http://localhost:8000/admin** and log in with the user you
just created.

And there we have it:

![](http://codeinstitute.wpengine.com/wp-content/uploads/2016/11/1479225809_image3.png)

  
Go ahead and click on **Todos** and we should get the following:

![](http://codeinstitute.wpengine.com/wp-content/uploads/2016/11/1479225809_image4.png)

  
When we click on **Add Todo**, we’ll see the following:

![](http://codeinstitute.wpengine.com/wp-content/uploads/2016/11/1479225809_image5.png)

  
Go ahead and create some **todo** records and then we’ll have a look at how we
can **serialize** that data!

 

**COMPLETED CODE**  
The code for this lesson can be found
at <https://github.com/Code-Institute-Org/full_stack_solutions/tree/master/Stream-Three/django-todo/part_1/django_todo>
