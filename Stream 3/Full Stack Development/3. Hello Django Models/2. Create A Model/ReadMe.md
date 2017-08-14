### CREATE A MODEL

We’ll continue to work on our ModelTest project in this unit. Let’s hold off
creating a view for now and focus on creating models instead:

1.  Open **models.py** in your app.

    -   All models subclass the base Model class, and contain field definitions.

2.  Create a new class called **Contact** that inherits from
    the **Model** class.

3.  Add a **Meta** class to successfully build the class in Sublime text.

 

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.db import models
 
class Contact(models.Model):
 
    class Meta: # include this to ensure build in IDE
        app_label = "ModelTest_app"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1.  Add some field definitions:

    -   Each field is represented by an instance of a **Field** subclass. We’re
        using CharField for character fields. This tells Django what type of
        data each field will hold.

    -   The name of each Field instance
        (**first_name**, **last_name**, **mobile**) is used as an attribute for
        the **Contact**model class, and is also used as the column name in our
        database.

    -   We also impose a character length restriction on the values passed to
        each field by passing a required **max_length** argument into the
        CharField constructor. This prevents our app from storing strings that
        are too big for our requirements. We’ve set our mobile string length to
        be up to 20 characters, which should cover pretty much all cell phone
        number configurations.

 

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.db import models
 
class Contact(models.Model):
 
    class Meta: # include this to ensure build in IDE
        app_label = "ModelTest_app"
 
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=20)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1.  Update the database with the new table from our Contact model:

    -   First, run **python manage.py makemigrations**

    -   Then run **python manage.py migrate**

  
  


![](http://codeinstitute.wpengine.com/wp-content/uploads/2015/11/1448898161_image7.png)

  
  
  
The **makemigrations** command essentially lets Django know that changes were
made to the models and that we want to create a migration. We then need to apply
the migration to create the actual database tables. You’ll do this any time you
add a new model or make changes to an existing one.

Find out more about
migrations [here.](https://docs.djangoproject.com/en/stable/topics/migrations/)
