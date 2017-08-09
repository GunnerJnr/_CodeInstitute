### VIEWS AND URLS

In the next two lessons, we’ll create a project called HelloWorld_prj and we’ll
learn how to say Hello, World! with Django.

Topics include:

-   Installation

-   Create a project

-   View the basics

-   Create an app

-   Register the app

-   Create a view

### INSTALLATION

1.  Open the command line interface and create a new directory
    called **hello_django**:

    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    mkdir hello_django
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

2.  Create a virtual environment inside the directory using virtualenv env:

    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    virtualenv env
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

3.  Activate the virtual environment:

    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    env\Scripts\activate
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

4.  Install the latest version of Django:

    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    pip install django
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

5.  Check that it was installed correctly by opening the python shell and
    running:

1  
2

import django  
print django.VERSION

### CREATE A PROJECT

In keeping with tradition, we’ll create a project that outputs Hello, World! And
what do we need to do to achieve such feat? Take a look below to find out.

1.  Create a new project called **HelloWorld_prj**

![](http://codeinstitute.wpengine.com/wp-content/uploads/2015/12/1449675915_image5.png)

  
  


1.  This creates the elements of your project, consisting of two directories and
    five files (note we’re using the command-line tool named `tree` to print the
    file layout, but you don’t need to have it yourself):

![](http://codeinstitute.wpengine.com/wp-content/uploads/2015/12/1449675915_image6.png)

  
  
  
The root folder (**HelloWorld_prj**) containing our project is just a holding
directory and can be renamed to anything you like.

-   **manage.py**: Perfoms admin tasks for your project, such as putting it on
    the system path, or starting the built-in webserver.

-   **settings.py**: This is the settings file for your project, where you
    define your project’s configuration settings, including database
    connections, other applications, templates, and more.

-   **urls.py**: The url declarations for this Django project. This file
    contains a list of mappings which connect urls to views.

-   **wsgi.py**: An entry-point for WSGI-compatible web servers to serve our
    project. This file handles our requests/responses to/from Django development
    server.

-   **\__init__.py**: An empty file that informs Python that this directory
    should be considered a Python package.

For now we’ll focus on **settings.py**, **urls.py**, and **manage.py**.  
  
  


### VIEW THE BASICS

Let’s view the basic project in a web browser. To do this, we need to start
Django’s built-in web server.  

1.  Navigate to the project root folder and fire up the web server. Ignore the
    migrations warnings for now.

![](http://codeinstitute.wpengine.com/wp-content/uploads/2015/12/1449675915_image7.png)

  
  


1.  Open a browser window and type in the URL **http://localhost:8000** 

![](http://codeinstitute.wpengine.com/wp-content/uploads/2015/12/1449675915_image8.png)

  
  
  
And we’re off! This is the default rendered Django project view.  
  
  


### CREATE AN APP

Navigate to the root **HelloWorld_prj** directory and create an app
called **HelloWorld_app**:

![](http://codeinstitute.wpengine.com/wp-content/uploads/2015/12/1449675915_image9.png)

  
  
  
This adds a new app directory and app files ready for our functionality to be
added.

![](http://codeinstitute.wpengine.com/wp-content/uploads/2015/12/1449675915_image10.png)

  
  


-   **admin.py**: This is used to register an app’s models with the admin
    interface.

-   **models.py**: This is where our data entities (tables) and their
    relationships are created and accessed.

-   **tests.py**: This is where our application test code is stored.

-   **views.py**: This fie acts as the controller for you application. Your
    business logic lives in here and deals with request from and responses to
    the server.

  
  


### REGISTER THE APP

Our project needs to know that the app exists. To enable this, we need to
register the app in **settings.py** of our project.

The easiest way to work with Django projects is through a combined use of
Sublime Text and the command line interface. So let’s open our
root **HelloWorld_prj** folder in Sublime Text.

1.  Open **settings.py**.

2.  Add our app to the **INSTALLED_APPS** tuple.

![](http://codeinstitute.wpengine.com/wp-content/uploads/2015/12/1449675915_image11.png)
