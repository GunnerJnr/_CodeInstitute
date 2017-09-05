How to Create a Set of Configuration Files to Describe How Your App Should be Installed
=======================================================================================

##### In this unit the students will learn how to create a setup.py file that will the to reuseable Python packages

 

### HOW TO CREATE A SET OF CONFIGURATION FILES TO DESCRIBE HOW YOUR APP SHOULD BE INSTALLED

We need to create a new folder outside of our Django project folder called
‘reusable_blog_app’, which will contain our restructured app and a few
configuration files that will instruct ‘pip’ on how to build and install our app
in other projects.

![](http://codeinstitute.wpengine.com/wp-content/uploads/2016/01/1452278888_image4.png)

In here, we need to copy the contents of our blog app into a new folder called
‘reusable_blog’, which will be the name we’re going to package our blog as.

   
It is important to name your packages with unique names that won’t conflict with
any existing packages. For instance, avoid using names such as ‘auth’ or
‘admin’. These are built-in packages in the Django framework and would certainly
conflict with your own naming convention.

In addition, we need to create the LICENSE, README.rst, MANIFEST.in, and
setup.py files, which are all just text files.

LICENSE is just a place to state what license you are making your app available
under, and can be anything from BSD, GPL, or public domain, if you don’t really
care how it is used.

README.rst is a file that will be displayed on our Github page to give
instructions on how to install and use the app.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
=====
Blog
=====
 
Blog is a reusable blog app for Django
 
Detailed documentation is in the "docs" directory.
 
Quick start
-----------
 
1. Add 'reusable_blog' to your INSTALLED_APPS setting like this::
 
    INSTALLED_APPS = (
        ...
        'reusable_blog',
    )
 
2. Include the polls URLconf in your project urls.py like this::
 
    url(r'^blog/', include('reusable_blog.urls')),
 
3. Run `python manage.py migrate` to create the blog models.
 
4. Add the blogs css::
    <link rel="stylesheet" href="{% static "css/blog.css" %}">
 
5. Add a link to the blog in the base.html
    <li><a href="/blog/">Our Blog</a></li>
 
6. Visit http://127.0.0.1:8000/blog/ to view the blogs you create.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  
`MANIFEST.in` contains instructions for our setup.py so that it will know that
our static files and code files need to be included in the package. The process
would normally only expect the package to contain code. Because it is a Django
app, we are adding in the templates and static files:

include LICENSE  
include README.rst  
recursive-exclude reusable \*.pyc  
recursive-include reusable_blog \*.css  
recursive-include reusable_blog \*.html  
recursive-include reusable_blog \*.py

  
Here, we specifically include our `LICENSE` and `README.rst` and then
use `recursive-exclude` to avoid adding any .pyc files. That way, we force the
code to be compiled on the server’s side.

We finally use `recursive-include` to add any css, html, and py files it finds
in the reusable_blog folder.

These rules will ensure that we include all the code and all the needed assets
for the app to be installable and usable in other projects.

Our setup.py file is of real interest, as we’re going to create a Python package
using Python (it’s like *Inception*!).

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import os
from setuptools import setup
 
with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()
 
# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))
 
setup(
    name='reusable-blog-app',
    version='1.0.0',
    packages=['reusable_blog'],
    include_package_data=True,
    license='BSD License',  # example license
    description='A simple Django app to create blogs',
    long_description=README,
    url='http://www.example.com/',
    author='Your Name',
    author_email='yourname@example.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License', # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires = [
        'Pillow',
        'django_forms_bootstrap',
        'django-disqus',
    ],
)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Here, we import setup from `setuptools` and use it to describe our package.

When we use pip later to install the package, it will clone the code from
GitHub, install, and compile our code and assets based on this and what’s in the
MANIFEST file.

We’ve left some of the settings for you to choose what you want, like the email
address, for instance. The url is often set to the website for your package, and
would probably best be set to your GitHub page.

`classifiers` is used to describe what categories this app could be catalogued
under, if someone was to search for apps that fulfilled certain functions.

`install_requires` is where we specify the dependencies for our app. In our
case, we need `Pillow` for our ImageFields, `django_forms_bootstrap` for
rendering our forms, and Disqus to integrate with disqus.com. Concerning disqus,
note that you’d also need to set the **DISQUS_WEBSITE_SHORTNAME** constant in
the settings of each project that relies on this app, which makes good sense,
since each such project would generally want to use a different disqus setup.

We need to list them here so that when we install the package via pip, they will
be installed too.
