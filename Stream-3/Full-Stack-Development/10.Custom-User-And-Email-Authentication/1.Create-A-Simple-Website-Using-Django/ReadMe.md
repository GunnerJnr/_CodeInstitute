### CREATE A SIMPLE WEBSITE USING DJANGO

Start by creating a new Django project called auth_demo to host the
authentication feature that we are about to build. The project will be similar
to the simple website you created for learning about flatpages.  

Create the project using PyCharm and remember the following steps:

-   **Create a Virtual Environment**

    When creating the project, create a virtual environment for the project’s
    dependencies.

    Click the 

    ![](http://codeinstitute.wpengine.com/wp-content/uploads/2016/02/1455725435_image2.png)

    next to the ‘Interpreter’ setting and enter the path to the virtual
    environment.

    ![](http://codeinstitute.wpengine.com/wp-content/uploads/2016/02/1455725435_image3.png)

-   **Create an app for the landing page**

    Create an App called ‘hello’ to host the landing page. Use the terminal
    window in PyCharm.

    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    $ python manage.py startapp hello
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-   **Create an app for the authentication code**

    Create an App called ‘accounts’ to host the authentication code. Use the
    terminal window in PyCharm.

    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    $ python manage.py startapp accounts
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-   **Install django-forms-bootstrap**

    We plan on using Bootstrap to style our forms, so go ahead and install the
    django-forms-bootstrap  
    pip package:

    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    $ pip install django-forms-bootstrap
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-   **Create a Landing Page**

    Create a base.html file in the templates folder:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
{% load staticfiles %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Our Simple Site</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootswatch/3.3.6/cerulean/bootstrap.min.css">
</head>
<body>
<div class="container">
   <div class="masthead">
       <ul class="nav nav-pills pull-right">
           <li><a href="#">Home</a></li>
           <li><a href="#">About</a></li>
           <li><a href="#">Contact</a></li>
           <li><a href="#">Register</a></li>
           <li><a href="#">Log In</a></li>
           <li><a href="#">Log Out</a></li>
       </ul>
       <h1><span class="fui-settings-16 muted">Our Simple Site</span></h1>
   </div>
   <hr>
    {% if messages %}
        <div class="alert alert-success">
            <div class="messages">
                {% for message in messages %}
                    {{ message }}
                {% endfor %}
            </div>
        </div>
    {% endif %}
 
 
   <div class="container">
       {% block content %}
       {% endblock %}
   </div>
   <hr>
   <div class="footer">
       <p>Made By Bootcampers and Django </p>
   </div>
</div>
</body>
 
<!-- script references -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.7/js/bootstrap.min.js">
</script>
</html>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-   **Create an index.html file in the templates folder**

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
{% extends 'base.html' %}
{% block content %}
    <h2>Hello, World!</h2>
    <p>Our very simple site</p>
{% endblock %}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-   **Render the landing page by editing views.py in the hello app**

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.shortcuts import render
 
# Create your views here.
def get_index(request):
    return render(request, 'index.html')
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-   **Add a link in ‘urls.py’ to the landing page view**

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from hello import views
... 
urlpatterns = [
    ...    
    url(r'^$', views.get_index, name='index'),
]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-   **Add the ‘hello’ app to Installed Apps in ‘settings.py’**

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
INSTALLED_APPS = [
    ...
    'hello',
]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-   **Run the server to check your work**

    ![](http://codeinstitute.wpengine.com/wp-content/uploads/2016/02/we-are-social.png)

    Note the links for Register, Log In, and Log Out. The remainder of this unit
    will focus on getting these to work.
