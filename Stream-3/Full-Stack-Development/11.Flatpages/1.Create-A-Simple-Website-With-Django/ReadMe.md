Create a Simple Website with Django
===================================

##### In this unit the students will learn how to create a small, simple website using Django

 

Please note due to this being a lesson containing only two tasks that both glue
together all the code for this lesson can be found in the folder for the second
part of the lesson also, but so you can see what was asked for the first part of
the lesson I have included the lessons instruction below.

 

### CREATE A SIMPLE WEBSITE WITH DJANGO

In this unit, we’ll start by creating a new Django project
named **we_are_social**, which we’ll be expanding this project in several stages
throughout the following units.

The example code for the we_are_social project will include the **accounts** app
that you previously created (in the **Custom User & Email
Authentication** lesson). You don’t have to, but we recommend that you manually
include this app in your new project too. Later on in the stream, we will have a
lesson explaining how to create a fully reusable app, but for now, we suggest
copying the app code manually to better practise the different parts of a Django
project.

Next, after creating the we_are_social project and (optionally) adding the code
for the accounts app, go ahead and create a new app called hello, using `python
manage.py startapp hello`.

 

### ADD A LANDING PAGE

Now that the main app is up, let’s add a basic landing page.

-   In the views.py file of the hello app, add the following to get a view up
    and running:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def get_index(request):
   return render(request, 'index.html')
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-   Next, we add a new pattern to our Project’s urls.py. Import views, then add
    a url pattern to call the get_index function.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from hello import views
urlpatterns = [
...
    url(r'^$', views.get_index),
]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-   In the templates folder of the hello app, create a HTML file called
    index.html. PyCharm will auto generate the code for a basic html page. Add
    some content between the \<body\>\</body\> tags, as shown below:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<h1>Hello, World!</h1>
<p>Our very simple site</p>
</body>
</html>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-   Run your server to test your work.

![](http://codeinstitute.wpengine.com/wp-content/uploads/2016/02/1455289439_image1.png)

### ADD AN ABOUT PAGE USING FLATPAGES

Flatpages makes it very easy to provide rudimentary content management features
to your users. This allows them to edit some pages on their site on their own,
without needing to call on developers.

While you aren’t required to install any additional modules with pip, you can’t
just use flatpages ‘out of the box’. You need to include some configuration
settings into your settings.py file and maybe, depending on the circumstances,
your urls.py too.

 

### CONFIGURE FLATPAGES

If you are working with a newly created application, you will need to create the
required database tables and user login details.

-   Run the migrate command to set up our admin tables in our SQLite database

-   Create an admin user (by running `python manage.py createsuperuser`)

-   Log in to the admin panel to check that everything is set-up correctly. Note
    that there is no ‘Flatpages’ section within the admin dashboard.

Now, let’s set up Flatpages.

-   Add the following two lines to the INSTALLED_APPS settings:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
INSTALLED_APPS = (
...
  'django.contrib.sites',
  'django.contrib.flatpages',
)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-   Create a SITE_ID value in settings.py

So that we can get things up and running, we need to add a SITE_ID to our
setting so Django knows which site we are running from. Add this above your
INSTALLED_APPS section:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
SITE_ID = 2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

### NOTE

We give this a value of 2 because the database will already contain an entry for
‘example.com’ with a SITE_ID of 1. In case there is already more than one site
in your database, you might need to use a higher SITE_ID here; check the
django_site table in the database to find the last id.

 

-   Run the migrate command again and the database tables for these apps will be
    created.

-   Configure the flatpages middleware to take care of our routes.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
MIDDLEWARE = (
...
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Each time you visit a page that doesn’t have a configured route, a 404 error is
created within the system. Flatpages works by intercepting 404 errors and
checking in the database for a flatpage that matches that url. If it finds one,
it will display this instead of the 404 page error.

-   Configure the url routing for flatpages. Add the following to urls.py

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.conf.urls import url, include
urlpatterns = [
    ...
    url(r'^pages/', include('django.contrib.flatpages.urls')),
]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Note that the include function is imported from django.conf.urls. You already
import ‘url’ from that library. You can simply append ‘include’ to that
statement rather than having a separate import statement.  

-   Log into the Admin Panel. Note that there is now a Flat Pages section.

![](http://codeinstitute.wpengine.com/wp-content/uploads/2016/02/1455289439_image2.png)

-   We will be running the flatpages locally, so we need to add localhost as a
    site. Click Add in the Sites section. Enter localhost and click save.

![](http://codeinstitute.wpengine.com/wp-content/uploads/2016/02/1455289439_image3.png)

-   We need to create a template that will be used for our flatpage content.
    This template can be as elaborate as you wish. You will probably want to
    style extend an existing template in your application, so that your
    flatpages are consistent with the rest of the site. For now, we’ll make the
    simplest possible template that will work. Under the templates directory,
    create a subdirectory named flatpages and add a Html file named default.html
    to that folder.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
{% block content %}
   <h2>{{ flatpage.title }}</h2>
   {{ flatpage.content }}
{% endblock %}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
