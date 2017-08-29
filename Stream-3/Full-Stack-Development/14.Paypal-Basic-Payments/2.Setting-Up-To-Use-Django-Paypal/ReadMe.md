### SETTING UP TO USE DJANGO-PAYPAL

Now that that’s done, let’s open our we_are_social project and the first thing
we’re going to do is install Django-Paypal. So open up terminal in Pycharm and
activate your virtualenv. After this, run the following command:

`pip install django-paypal==0.3.6`

Next, add some settings to our settings.py:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# PayPal Settings
SITE_URL = 'http://127.0.0.1:8000'
PAYPAL_NOTIFY_URL = 'http://127.0.0.1/a-very-hard-to-guess-url/'
PAYPAL_RECEIVER_EMAIL = '<your paypal merchant email goes here>'
 

INSTALLED_APPS = [
…
   'paypal.standard.ipn',
…
]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The `SITE_URL` setting will help when we define where PayPal should return our
customer after they’ve bought our products.

`PAYPAL_NOTIFY_URL` is used by Django-Paypal to record transactions in the
database. However, we’re not going to be using it with basic payments in this
unit – but we still need it nonetheless to support PayPal’s way of
handling things.

The part about *a-very-hard-to-guess-url* is there to show that this URL should
normally be a randomly generated string that should make it very hard indeed to
guess, thus avoiding the potential abuse or misuse of the payment system.

`PAYPAL_RECEIVER_EMAIL` is the email address of the person who will be given the
funds for any transactions. For us, that will be the merchant email address that
we setup earlier in the developer section of the PayPal website.

Once that’s out of the way, we can go ahead and create a new app
called `paypal_store` by running `python manage.py startapp paypal_store` in the
terminal. Then in Pycharm click on *File*then click on *Synchronize*.

And don’t forget to add `paypal_store` to the `INSTALLED_APPS` in settings.py!

### URLS

Django-Paypal also needs us to setup our urls.py so we can have communication
back from PayPal about successes and failures in payments.

Let’s add these to our we_are_social urls.py:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.conf.urls import url, include
from paypal.standard.ipn import urls as paypal_urls
from paypal_store import views as paypal_views
 
urlpatterns = [
    ...
    url(r'^a-very-hard-to-guess-url/', include(paypal_urls)),
    url(r'^paypal-return', paypal_views.paypal_return),
    url(r'^paypal-cancel', paypal_views.paypal_cancel),
]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Besides including our own *a-very-hard-to-guess-url* with the Django-Paypal
URLs, we also include two Paypal URLs to handle the return of a customer after
payment, and also what happens when they cancel at the PayPal site. In order to
do that, we’ll need to add the following to the views.py file in our
paypal_store app:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
 
 
@csrf_exempt
def paypal_return(request):
    args = {'post': request.POST, 'get': request.GET}
    return render(request, 'paypal/paypal_return.html', args)
 
 
def paypal_cancel(request):
    args = {'post': request.POST, 'get': request.GET}
    return render(request, 'paypal/paypal_cancel.html', args)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Let’s create a new folder in our templates directory called *paypal*, and in
that folder we’re going to create the following HTML pages.

First let’s create *paypal_cancel.html*:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
{% extends "base.html" %}
{% block content %}
    <h1>You've cancelled the purchase of this item!</h1>
 
    <h2>POST</h2>
    {{ post }}
 
    <h2>GET</h2>
    {{ get }}
{% endblock %}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

And now we’ll create *paypal_return.html*:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
{% extends "base.html" %}
{% block content %}
    <h1>Thanks for buying my item :)</h1>
 
    <h2>POST</h2>
    {{ post }}
 
    <h2>GET</h2>
    {{ get }}
{% endblock %}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
