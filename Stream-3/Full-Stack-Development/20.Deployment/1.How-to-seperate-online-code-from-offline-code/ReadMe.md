How to Separate Online Code From Offline Code
=============================================

##### In this unit the students will learn how to separate their online code from their offline code by using multiple settings files in Django

 

### HOW TO SEPARATE ONLINE CODE FROM OFFLINE CODE

So now that we’re going to be hosting production code, there’s some changes that
we need to make to our project structure before we can host our code.

Usually when working in an industry, there will be a certain process that your
projects will go through. The steps in this process are:

  
**1. Dev** – This is the development stage, the normal process that we’ve be
using so far. Basically what will happen is that you’ll develop your features
and work on your bug fixes. Then these will be committed and pushed to your
version control (Github, Subversion, etc.). Depending on the environment that
you work in, this development process may last for a week to a month or maybe
longer. Once all the features and bug fixes are in place, they’ll move to the
Staging process.

**2. Staging** – Once the development process is complete, the code is then
moved to a staging environment. The purpose of a staging environment is to serve
as a test bed before release – so a staging should mimic the production
environment. Once the code is in the staging environment, the testers will test
the application in order to find any bugs or issues and report them back to the
developers so they can be fixed before going to production. Once the staging
code has been declared stable, then it’s moved to production.

**3. Production** – This is it! Once you’ve reached this point, your code is now
being used by your customers/users. One thing to be wary of is the fact that,
just because the code made it to production, that doesn’t mean that it will be
bug free. Although every effort is made to make the release as bug free as
possible, sometimes lower priority bugs are allowed into production and will be
worked on in a later release.

  
  
  
With this in mind, let’s create our different environments within
our **we_are_social** project.

The first thing we’ll to do is create a new python package called **settings**.
Once we’ve done that we can create a new Python file called **base.py**. This
will act as our base settings file and will contain settings that will be shared
across all our environments.

Now that we’ve got that done, let’s go ahead and add some code:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import os
 
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
 
# SECURITY WARNING: Enter your own SECRET_KEY here
SECRET_KEY = '<SECRET_KEY>'
 
ALLOWED_HOSTS = []
SITE_ID = 2
 
# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django_forms_bootstrap',
    'paypal.standard.ipn',
    'rest_framework',
    'tinymce',
    'emoticons',
    'disqus',
    'reusable_blog',
    'home',
    'accounts',
    'paypal_store',
    'products',
    'magazines',
    'threads',
    'polls',
]
 
AUTH_USER_MODEL = 'accounts.User'
AUTHENTICATION_BACKENDS = ('django.contrib.auth.backends.ModelBackend',
                           'accounts.backends.EmailAuth',)
LOGIN_URL = '/login/'
 
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
]
 
ROOT_URLCONF = 'we_are_social.urls'
 
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
 
WSGI_APPLICATION = 'we_are_social.wsgi.application'
 
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
 
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
 
STATIC_URL = '/static/'
STATIC_ROOT = ''
 
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)
 
TINYMCE_JS_ROOT = os.path.join(BASE_DIR, "static", "js",
                               "tinymce", "tinymce.min.js")
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You’ll notice that this is basically just our **settings.py** file, although
there are a couple of things that we left out – such as the database connection,
debug mode, and our Stripe and Paypal settings. We’ve also removed
the **debug_toolbar** from the INSTALLED_APPS as we don’t want our users to be
able to see our debugging info!

Once we’ve done this, then we need to go ahead and create a new file in
our **settings** directory called **dev.py**. This file will provide the
settings that we’ll use for our development environment:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from base import *
 
DEBUG = True
 
INSTALLED_APPS.append('debug_toolbar')
 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
 
# Stripe environment variables
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', '<your STRIPE_PUBLISHABLE key>')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', '<your STRIPE_SECRET key>')
 
# Paypal environment variables
SITE_URL = 'http://127.0.0.1:8000'
PAYPAL_NOTIFY_URL = '<your ngrok URL>'
PAYPAL_RECEIVER_EMAIL = '<your Paypal merchant email>'
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

What will happen here is that we’ll tell Django which environment to use
whenever we run any of our **manage.py** commands.

For example:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
python manage.py runserver --settings=settings.dev
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Next we’ll create a new file called **staging.py** and in there we’ll add the
following:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from base import *
 
DEBUG = False
 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
 
# Stripe environment variables
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', '<your STRIPE_PUBLISHABLE key>')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', '<your STRIPE SECRET key>')
 
# Paypal environment variables
PAYPAL_NOTIFY_URL = 'https://291e2d8f.ngrok.io/a-very-hard-to-guess-url/'
PAYPAL_RECEIVER_EMAIL = 'aaron@codeinstitute.net'
 
SITE_URL = 'https://your-heroku-app.herokuapp.com'
ALLOWED_HOSTS.append('your-heroku-app.herokuapp.com')
 
# Log DEBUG information to the console
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

### NOTE

We’ve set up our database connect to use the SQLite database as our database for
now. If you haven’t added you SQLite database to your .gitignore file then
you’ll be able to continue using the data that you used up until this point.
However, if the database file has been added to the .gitignore file then a fresh
database will be created when we run the migrate command later.

 

Note about that since in **staging.py** we don’t have `DEBUG = True` set, we
need to explicitly tell Django where to log all errors and other details about
our project; that’s why we added a LOGGING configuration. By specifying
‘console’ in there, that means that all the messages will be available for us to
view on heroku in the **View logs** option inside the **More** menu on the
dashboard, as well as by running `heroku logs` locally. And we can change the
DJANGO_LOG_LEVEL to get other levels of detail, with the default we’ve set here
(‘DEBUG’) being the most verbose.

We’ve left out our Paypal settings for now because we’ll need to set up our
Heroku app first. We’ll add them in once our Heroku app is configured.

Now that we have our new setting file, we can go ahead and delete the
settings.py file in our we_are_social directory.

Next we’ll need to make sure we have the correct dependencies for each of the
environments. Let’s do this now by creating a new folder in our projects root
and call it **requirements**.

Within that new folder we’ll create a new file called **base.txt** and in that
file we’ll add the following:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
arrow==0.7.0
beautifulsoup4==4.4.1
django-disqus==0.5
Django==1.8.9
django-emoticons==1.1.2
djangorestframework==3.3
django-forms-bootstrap==3.0.1
django-tinymce==2.2.0
Pillow==3.1.1
python-dateutil==2.4.2
six==1.10.0
wheel==0.24.0
django-paypal==0.2.7
stripe
git+https://github.com/<your Github Username>/reusable-blog-app.git
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

### NOTE

The above packages have the specific version numbers that we tested and are
known to work well, but you might find it better to remove the version numbers
and try the latest versions instead. To fit better with the rest of your
project’s dependency versions.

 

Next we’ll create another file called **dev.txt** and inside here we’ll need to
reference the **base.txt**file in order to install the dependencies common
across all environments, as well as **django-debug-toolbar**:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
-r base.txt
django-debug-toolbar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

The first line here (**-r base.txt**) will install everything from
the **base.txt** file. What we’re saying here is that we want to install
everything from base.txt and then install whatever else we need for the dev
environment. In this case it’s django-debug-toolbar.

After that we’ll create a new file called **staging.txt**. Again we’ll
reference **base.txt**. As well as that, we’ll also need to add a reference
to **mysql-python** as we’ll be using a MySQL database:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
-r base.txt
mysql-python==1.2.5
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Lastly, we’ll update the **requirements.txt** in our project’s root directory.
We need to do this because Heroku will look for a **requirements.txt** file in
our root directory so we need to tell it to use our **staging.txt** file for the
dependencies:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
-r requirements/staging.txt
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Now that we’ve got our environments ready, let’s go ahead set up Heroku to host
our app and configure our MySQL database.  

