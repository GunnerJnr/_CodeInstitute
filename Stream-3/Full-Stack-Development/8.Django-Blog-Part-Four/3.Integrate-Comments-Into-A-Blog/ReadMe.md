### INTEGRATE COMMENTS INTO A BLOG

As of Django 1.8, the default comments module is no longer supported due to spam
vulnerability. Third party products recommended **Disqus**, written in Django.
To use Disqus in Django, we need to access its API.

1.  Sign up to Disqus and create a new
    application: <https://disqus.com/api/applications/register/>

2.  Once registered, fill out the form as per below:  
    

    ![](http://codeinstitute.wpengine.com/wp-content/uploads/2016/01/1453160720_image5.png)

      
    The most important fields are:

    -   **Label** – this forms our unique identifier for your comments app.
        Choose any label you like, as long as it doesn’t have any spaces in it.

    -   **Website** – we need to set this to our localhost
        (`http://localhost:8000`) when testing locally. This can be changed
        later.

3.  Next we install django-disqus to integrate with our Django project: **pip
    install django-disqus**

4.  Add an entry to Installed Apps for **disqus** and **django.contrib.sites**:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
INSTALLED_APPS = [
...
 'django.contrib.sites',  
 'disqus'
]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Run `python manage.py makemigrations` and `python manage.py migrate` to create
the django_site db table.

-   Add the following two entries to **settings.py** where ‘yourshortname’ is
    the app name you registered with disqus and the site id matches the one in
    your django_site db table.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
DISQUS_WEBSITE_SHORTNAME = 'yourshortname'
SITE_ID = 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Add tags to **postdetail.html** to associate comment with a post:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
{% load disqus_tags %}
{% set_disqus_title post.title %}
{% disqus_show_comments %}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

-   Voila!
