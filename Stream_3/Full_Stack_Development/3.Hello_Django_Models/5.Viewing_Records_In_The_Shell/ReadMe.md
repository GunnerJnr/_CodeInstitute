### VIEWING RECORDS IN THE SHELL

You might want to list the records in your table. To do this, run the
command **Contact.objects.all()**

![](http://codeinstitute.wpengine.com/wp-content/uploads/2015/11/1448898161_image15.png)

There are two records in the table – each one represented by the list
entry: **(Contact: Contact object)**

This representation isn’t very useful because it doesn’t tell us much about each
record, other than it exists. We can fix this by adding a
 \*\*__str__()\*\* function to our model.

Take a look at an example below and add it to your code. What we’ve done here is
join the first and last names of the contact as the string representation of the
object.

![](http://codeinstitute.wpengine.com/wp-content/uploads/2015/11/1448898161_image16.png)

Save and build your code. Then exit the shell and enter it again. Import the
model and run the **Contact.objects.all()** command again. You should see
something similar to below:

![](http://codeinstitute.wpengine.com/wp-content/uploads/2015/11/1448898161_image17.png)

### SUMMARY

In this lesson, we’ve learned that:

-   Django supports ORM through models

-   All model classes inherit from the **models.Model** class

-   Model attributes map to database table fields

-   Python comes with the SQLite DBMS

-   Django projects are pre-configured to use SQLite, but can also use other
    DBMSs

-   To  populate our database, we must first run the migrate command

-   We run the makemigrations command followed by the migrate command after
    adding a new model or modifying an existing one

-   SQLite has a free GUI-based administration application called SQLite
    Database Browser available, which you can use to view your project database
    and its tables

-   You can populate your models with data through the Python shell

In the next lesson, we’ll learn how to add data through Django’s built-in admin
screen, and we’ll also bind our model to a view and display the result in a
Template.
