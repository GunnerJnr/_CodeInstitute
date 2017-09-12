### USE EXTERNAL MODULES TO ‘COMPOSE’ YOUR APPS

The point of our We Are Social site is to to get people together to share
business ideas that have a benefit to society. Now that our application is
taking shape, let’s create a forum where our site members can chat and thrash
out these ideas. We’ll begin by opening our existing *we_are_social* project.

Now we’ll start composing’ our forum by installing a few handy modules to add to
our forum:

pip install arrow  
pip install django-emoticons  
pip install django-tinymce  
pip install django-debug-toolbar

Let’s take minute to look at the new
modules: **django-emoticons**, **django-tinymce**, and **django-debug-toolbar**.

 

### DJANGO-EMOTICONS

**django-emoticons** will assist us in processing our posts’ content and also
replacing any emoticons like `:)` or  
`:(` with a nice animated image to add some life to our posts.

![](http://codeinstitute.wpengine.com/wp-content/uploads/2016/01/1452537277_image2.png)

 

### DJANGO-TINYMCE

**django-tinymce** adds in a WYSIWYG text editor that can be used in our forum –
as well as the admin when editing text – and provides a simple way of doing some
basic filtering of the user’s input to avoid having Javascript injection into
our site’s pages.

![](http://codeinstitute.wpengine.com/wp-content/uploads/2016/01/1452537277_image3.png)

 

### [DJANGO-DEBUG-TOOLBAR](https://lms.codeinstitute.net/course-status/#collapse_0eknpa)

**django-debug-toolbar** is technically not needed for our forum, but will be
invaluable to you when developing any application, as it provides a wealth of
information about each page as it loads.  
Add debug_toolbar to installed apps and add the following to the urls:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.conf import settings
from django.conf.urls import include, url
 
if settings.DEBUG:
    import debug_toolbar
    urlpatterns.append(url(r'^debug/', include(debug_toolbar.urls)))
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You will see this toggle in the top right corner of each page once you’ve
completed the **CONFIGURING MODULES**section:

![](http://codeinstitute.wpengine.com/wp-content/uploads/2016/01/1452537277_image4.png)

When you click it, the toggle will expand and give more information about your
page and what Django did to generate it:

![](http://codeinstitute.wpengine.com/wp-content/uploads/2016/01/1452537277_image5.png)

You can click each of these sections to see even more details about each
subject. If your pages are not displaying the way you thought they would, there
will be clues here!

 

### ADDITIONAL INSTALLS

Now we’ll need to make sure that in our **static** folder we have
a **js** and **css** folder.

We also need to install some Javascript to use the **tinymce** editor, as it is
actually a JavaScript library.

Next, head over to <http://www.tinymce.com/download/download.php> and grab a
copy of the latest version. It should download a zip file. Unzip this file to
anywhere on your machine. Once it’s unzipped, go into to the **tinymce** folder
and open up the **js** and copy the **tinymce** folder into our
project’s **‘static/js’** folder.

We also want to include some icons that can be used on our site as links to edit
or delete threads and posts instead of just having clickable text links, so head
over
to [https://fontawesome.github.io/Font-Awesome/](https://fortawesome.github.io/Font-Awesome/) and
download the Font Awesome icon toolkit by clicking *Download* on the main page.

That is also a zip file that we need to extract into our static folder under
the **‘static/css’** folder, so we can access it later.

### CONFIGURING MODULES

Now that we’ve installed our supporting modules, we need to do some coding to
set them up and include them into our project.

So let’s start with our settings.py and add our installed apps:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
    'debug_toolbar',
    'tinymce',
    'emoticons',
    'disqus',
    'reusable_blog',
    'home',
    'accounts',
    'paypal_store',
    'products',
    'magazines',
]
 
INTERNAL_IPS = ('127.0.0.1',)
MIDDLEWARE = [
…
'debug_toolbar.middleware.DebugToolbarMiddleware',
…
]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As well as this, we need to make some additional settings for our tinymce module
and font awesome:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
STATIC_URL = '/static/'
STATIC_ROOT = ''
 
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"), # static directory at the project level
)
 
# tinymce settings
TINYMCE_JS_ROOT = os.path.join(BASE_DIR, "static", 'js', 'tinymce', 'tinymce.min.js')
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This sets us up to use the JavaScript and css files we’ve installed, and
sets `TINY_JS_ROOT` for later when we use it in the admin. The setting will be
used to access the JavaScript library when rendering the textarea in our admin
forms.

Finally, we have our settings to instruct this instance of Django to use our
accounts.User model and the accounts.backend in the authentication process.

With all that work done, you are ready to go ahead and run the migrations to
install all the needed backend database support.
