###  

Security & Documentation
========================

Usually **HTTP requests** and **responses** are passed between the client and
server in pretty much plain text. Unfortunately, these requests and responses
can be intercepted by people that are up to no good! This will give them access
to any data you send to the server, and similarly, any data retrieved from the
server.

 

We can fix this though! We can use **SSL** (**Secure Socket Layer**) to encrypt
the messages sent to and from the server. Let’s take a look at how that would
work.

 

Fortunately it’s actually pretty simple and Django even has built in support for
it!  
We just need to make a slight adjustment to our **settings.py** file.

 

Go ahead and add the following settings:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

These settings don’t need to go anywhere specific, but somewhere after
the **INSTALLED_APPS** will do!

 

As well as this, we’ll need to set our **ALLOWED_HOSTS** setting. We need to add
our **localhost**and our Heroku domain.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
DEBUG = True
 
ALLOWED_HOSTS = ["127.0.0.1", "localhost", "<your heroku app>.herokuapp.com"]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

And that’s all there is to it. This will ensure that all **http** requests are
redirected to **https**. From now on, when making a request to the server, we’ll
have to use **https://\<heroku url\>.herokuapp.com/**.

 

We’re also going to have an issue with browser security, especially when working
from localhost. For example, the Angular app that we built in Stream One wasn’t
actually allowed to communicate with the server because of
Chrome’s **CORS** restrictions. In order to get around this issue, we need
whitelist localhost on the server. To do this, we need to
install **django-cors-headers**. We can either do this from Pycharm or from the
command line using:

`pip install django-cors-headers`

 

After that we’ll need to update some settings in **settings.py** file:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
INSTALLED_APPS = [
    ...
    'corsheaders',
    'todo',
    'accounts',
]
 
MIDDLEWARE = [
    ...
    'corsheaders.middleware.CorsMiddleware',
]
 
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_WHITELIST = (
    'http://localhost:8080',
    'http://127.0.0.1:8080',
)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

First we add **corsheaders** to the **INSTALLED_APPS**.

 

Then we add **corsheaders.middleware.CorsMiddleware** in
the **MIDDLEWARE** setting.

 

Lastly, we add some new settings to allow requests to be made
from **localhost**, including the **whitelist** where we
specify **http://localhost:8080** and **http://127.0.0.1:8080**.

   
The the URLs that need to be added to the **whitelist** should reflect the
address that you are trying to call the API from. For example, if you have an
Angular app running on **http://127.0.0.1:8080**, then that URL will need to
be **whitelisted**. If you have a Flask app that runs
on **http://127.0.0.1:5000**, then that URL will need to be added to
the **whitelist**. Only apps running on localhost will need to
be **whitelisted** – but if you app is hosted somewhere like Heroku, then it
should be fine!

 

You can add additional URLs to the whitelist setting as you need them. Go ahead
and push those changes up to Heroku.

 

But what now? Our API is complete. Since we’ve developed the API, we know what
URLs are available and what data they expect.

 

But what if someone else chooses to consume the API – how will they know this
information? For this we need to build some documentation. Usually this would be
a long and arduous process. But fortunately, people got sick of having to do
this and decided to build some tools to help us out!

One of these tools **drfdocs**.

 

**Drfdocs** plugs directly into the Django Rest Framework – so all we need to do
is install it, add it to our **INSTALLED_APPS**, and create a URL for it!

 

Once again we can install this through Pycharm or through the command line with:

`pip install drfdocs`

 

Once that’s done, we’ll add it to our **INSTALLED_APPS**:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_docs',
    'corsheaders',
    'todo',
    'accounts',
]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Lastly, we’ll update our **urls.py** in our **django_todo** directory:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.conf.urls import url, include
from django.contrib import admin
 
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^docs/', include('rest_framework_docs.urls')),
 
    # API
    url(r'^todo/', include('todo.urls')),
    url(r'^accounts/', include('accounts.urls'))
]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After that, we just create a new URL on **line 13**.

 

And that’s it! This is a great tool that will generate all of the documentation
for the API. It will even let you test the API, like we did
with **cURL** and **Postman**.  


### SUMMARY

In this lesson, we learned how to build the backend for the Angular app that we
created in Stream One.

 

We also took a look at how to **serialize** and **deserialize** data that gets
passed back and forth via the API using the Django Rest Framework.

 

We also took a look at how to secure our APIs against unwanted users by
using **JWT**s, as well as securing the communication with the server by
using **SSL** (**Secure Socket Layer**) and **HTTPS**.

 

Lastly, we looked at how we can expose the API endpoints and how we can use
different HTTP methods to access them in different ways.

 

All-in-all, this is a nifty lesson that should help you to understand APIs.
Continue building on this project and see what you can come up with!

 

APIs have become the cornerstone of modern web development. Pretty much all
mobile apps will rely on an API. All of their data will be stored in the cloud –
and when you register in an app, your app will be given a token that will be
used to authenticate against the server.

 

As well as mobile apps, a lot of web apps are also being built using an API.
Much like our Todo, they’ll expose an API on the backend, which will be consumed
by a Javascript framework such as Angular. There are a number of reasons for
this:

-   It increases separation of concerns by leaving the backend developers to do
    ther thing, without having to be involved in any of the front end and
    vice-versa.

-   It also means that developers don’t have to build an extra API into their
    existing app.

 

There are a multitude of other reasons, but we don’t need to concern ourselves
with those for now. For now, enjoy playing around with your API!
