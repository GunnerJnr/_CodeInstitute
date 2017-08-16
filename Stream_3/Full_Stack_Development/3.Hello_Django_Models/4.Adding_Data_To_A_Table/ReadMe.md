### ADDING DATA TO A TABLE

So how do we get data into our tables? First, we’ll add data via a Python shell,
and later we’ll learn how to make our life much easier via the admin interface.

1.  Adding data via python shell

    -   Run **python manage.py shell**

![manage.py](http://codeinstitute.wpengine.com/wp-content/uploads/2015/11/manage_py.png)

1.  Add a record to the contact table by creating an instance of model and
    updating its attributes, and saving the changes.

![](http://codeinstitute.wpengine.com/wp-content/uploads/2015/11/1448898161_image12.png)

1.  We can read back and even update our newly created record in the shell too.

![](http://codeinstitute.wpengine.com/wp-content/uploads/2015/11/1448898161_image13.png)

1.  Let’s have a look at the record using the SQlite Database Browser.

    -   Fire up the application and open your project database.

    -   Select the **ModelTest_app_contact** table.

    -   Select the Browse Data tab. You should see the record entry listed
        there.

![](http://codeinstitute.wpengine.com/wp-content/uploads/2015/11/1448898161_image14.png)

1.  Add another record to the table using the same method. Here’s a hint: create
    a new instance of **Contact**, access its attributes, and save your changes.
