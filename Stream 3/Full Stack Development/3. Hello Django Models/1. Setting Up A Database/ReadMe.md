### SETTING UP A DATABASE

Now that we have an understanding of how to create Django project from the
command line/terminal, let’s make life easier for ourselves by using Pycharm to
create a Django project.

Pycharm professional edition comes with a Django project template. Using the
template as our project type sets up all the necessary project elements. In
addition we can also access the command line/terminal for tasks like creating
and modifying databases, which we will come to shortly.  
  
  


### MIGRATE

Django itself will create some default helper database table for administration
purposes. We need to create these tables in the database before adding our own
custom tables. To do that, we use the **migrate** command. This creates the
database tables for all apps in INSTALLED_APPS whose tables have not already
been created. You will also use migrate to update your database with any changes
you make to your models, such as adding or removing fields (model class
attributes).

Let’s create a new project in PyCharm.

1.  In Pycharm create a new Django project (**File \> New Project**). You will
    be presented with a new project dialog box.

2.  Select Django from the left hand side of the **Create Project** dialog.

3.  Give the project a name of **ModelTest**

4.  Click on the Settings icon next to the Interpreter field and click
    on **Create VirtualEnv**  
      
      
    

    ![migrate](http://codeinstitute.wpengine.com/wp-content/uploads/2015/11/migrate.png)

5.  We are then presented with another dialog box where we are will give the
    virtualenv a name of **modeltestenv**and we’ll set the location to the
    virtualenv directory that we created when we first looked at virtualenv in
    Stream 2.  
      
      
    

    ![migrate2](http://codeinstitute.wpengine.com/wp-content/uploads/2015/11/migrate2.png)

6.  Click **OK**.

7.  Once the virtualenv has been created we can see that the Interpreter field
    has been updated and we can see that it refers to **modeltestenv**.  
      
      
    

    ![migrate3](http://codeinstitute.wpengine.com/wp-content/uploads/2015/11/migrate3.png)

8.  Expand the **More Settings** panel area and include an app
    called **ModelTest_app**  
      
      
    

    ![migrate4_new](https://lms.codeinstitute.net/wp-content/uploads/2015/11/migrate4_new.png)

9.  Click **Create**

In many cases, we need to edit **settings.py** with module-level variables
representing our Django settings. For example, we’ve seen that we edit the
settings file when registering applications with a project.

But take a look at the settings file in your new Django project and you’ll see
that because the **DATABASES**configuration uses SQLite by default, and SQLite
is included in Python, we don’t need to install or register anything else to
support our database.  
  


Once the project has been created, we’ll create our database and default admin
tables.

Run the following command in your project root directory (after activating the
virtualenv): **python manage.py migrate**

You should see something similar to below:  
  
  


![](http://codeinstitute.wpengine.com/wp-content/uploads/2015/11/1448898161_image3.png)

  
  
  
You’ll also have a new file added to your project called **Sqlite.db** in your
root directory.  
  
  


![](http://codeinstitute.wpengine.com/wp-content/uploads/2015/11/1448898161_image4.png)
