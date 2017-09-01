### SETUP PRODUCTS THAT REQUIRE SUBSCRIPTIONS

This is where we’re going to switch things up a bit from our last unit, in the
sense that we’re now going to add in some payment records for our magazines and
create code to check if our user has paid.

The first thing to do is to create our magazines app. Don’t forget to click
on *File* followed by *Synchronize* in Pycharm!

Once that’s done, we’ll add it to our settings.py:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
INSTALLED_APPS = [
    ...
    'magazines',
]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Next let’s open up our models.py file in our newly created magazines app and add
the following:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.db import models
from django.conf import settings
 
 
class Magazine(models.Model):
 
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
 
    def __unicode__(self):
        return self.name
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As in our previous unit, we have a `name`, a `description`, and a `price`. But
this time the price is the cost of our monthly subscription, not our one-off
payment.

Next, we define a new `Purchase` model that will let us link our Magazines to
users, and also tell if their subscription is valid.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
...
from django.utils import timezone
...
 class Purchase(models.Model):
 
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='purchases')
    magazine = models.ForeignKey(Magazine)
    subscription_end = models.DateTimeField(default=timezone.now)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To define a one-to-many relationship for our user and magazine, we use
the `ForeignKey` field type and we use the `related_name` option on our user, so
that when we want to look into the user’s purchase, we can
type `user.purchases` instead of `user.purchases_set`.

Let’s open up our accounts/models.py and modify our User model so it looks like
this:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class User(AbstractUser):
    objects = AccountUserManager()
 
    def is_subscribed(self, magazine):
        try:
            purchase = self.purchases.get(magazine__pk=magazine.pk)
        except Exception:
            return False
 
        if purchase.subscription_end > timezone.now():
            return False
 
        return True
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In our accounts.User model, we can now include a new method
called `is_subscribed` to check if the user is subscribed to a specific
magazine. And using our simpler naming convention, the code makes much more
sense.

   
We’re using a `try-except` here, because a search like this would generate an
exception if no records were found. To stop this from halting our code, we catch
the exception and return False instead.

### NEW TEMPLATE TAG

Because we’re creating a subscription, we need to pass information to PayPal
that they can return to us when the subscription is complete and later when the
subscription is cancelled. So we’re going to pass the user’s id and the
magazines’ id in a ‘custom’ field that PayPal supplies in its API.

Because of this, we can’t just create a form inside our model like before, as we
wouldn’t be able to easily access the current user’s id.

Instead, we’re going to create a custom template tag in
magazines/templatetags/magazine_extras.py to handle creating a form when passed
the user and magazine objects:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import uuid
from django import template
from django.conf import settings
from paypal.standard.forms import PayPalPaymentsForm
 
register = template.Library()
 
 
def paypal_form_for(magazine, user):
 
    if user.is_subscribed(magazine):
        html = "Subscribed!"
    else:
        paypal_dict = {
            "business": settings.PAYPAL_RECEIVER_EMAIL,
            "currency_code": "USD",
            "cmd": "_xclick-subscriptions",
            "a3": magazine.price,
            "p3": 1,
            "t3": "M",
            "src": 1,
            "sra": 1,
            "item_name": magazine.name,
            "invoice": uuid.uuid4(),
            "notify_url": settings.PAYPAL_NOTIFY_URL,
            "return_url": "%s/paypal-return/" % settings.SITE_URL,
            "cancel_return": "%s/paypal-cancel/" % settings.SITE_URL,
            "custom": "%s-%s" % (magazine.pk, user.id)
        }
 
        if settings.DEBUG:
            html = PayPalPaymentsForm(initial=paypal_dict,button_type='subscribe').sandbox()
        else:
            html = PayPalPaymentsForm(initial=paypal_dict,button_type='subscribe').render()
 
    return html
 
register.simple_tag(paypal_form_for)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Here we’re doing something a little more complex than before, as we’re first
checking if the user is already subscribed to the magazine. If they are, we skip
making the form altogether and return ‘Subscribed’.

If not, then we create our form using a dict with these values:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
...
        paypal_dict = {
            "business": settings.PAYPAL_RECEIVER_EMAIL,
            "currency_code":"USD",
            "cmd": "_xclick-subscriptions",
            "a3": magazine.price,
            "p3": 1,
            "t3": "M", # M = monthly
            "src": 1,
            "sra": 1,
            "item_name": magazine.name,
            "invoice": uuid.uuid4(),
            "notify_url": settings.PAYPAL_NOTIFY_URL,
            "return_url": "%s/paypal-return/" % settings.SITE_URL,
            "cancel_return": "%s/paypal-cancel/" % settings.SITE_URL,
            "custom": "%s-%s" % (magazine.pk, user.id),
        }
...
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The fields are similar to what we did before, but now we’re placing our price in
a field called `a3`. This is part of PayPal’s API scheme, and whilst it doesn’t
read easily from a human standpoint, it’s just one of those things we’ll have to
live with!

Notice that we’ve changed the invoice too, to only contain
the `uuid.uuid4()` value. We still need this to be unique so that PayPal will
allow the transaction to take place.

We’ve also moved our magazine id and user id to the `custom` field we spoke
about earlier:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
...
        paypal_dict = {
            ...
            "custom": "%s-%s" % (magazine.pk, user.id),
        }
...
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This should generate a string similar to ‘1-2’, where the magazine has an id of
1 and the user has id 2. This will be passed to PayPal. As we said, we’ll be
using this later to work out which user subscribed to what magazine.

Then we render the form in one of two ways; if we’re in *debug* mode, we use
the `sandbox()`method to return html for the form. If we’re not debugging (as in
live on a production server), we use `render()` to give us a form that points to
the live PayPal systems.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
...
        if settings.DEBUG:
            html = PayPalPaymentsForm(initial=paypal_dict, button_type='subscribe').sandbox()
        else:
            html = PayPalPaymentsForm(initial=paypal_dict, button_type='subscribe').render()
 
    return html
...
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Lastly, we register this new ‘simple_tag’ with the Django template system.

So let’s set up our template in **templates/magazines/magazines.html** to
contain the following code, such that as we iterate through our magazines (like
we did in the previous unit), we call our new template tag:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
{% extends "base.html" %}
{% load magazine_extras %}
{% block content %}
    <table class="table table-striped">
        <thead>
            <tr>
                <th>Name</th>
                <th>Description</th>
                <th>Price</th>
                <th>Subscribe</th>
            </tr>
        </thead>
        <tbody>
            {% for magazine in magazines %}
                <tr>
                    <td>{{ magazine.name }}</td>
                    <td>{{ magazine.description }}</td>
                    <td>${{ magazine.price }}</td>
                    <td>{% paypal_form_for magazine user %}</td>
                </tr>
            {% endfor %}
        </tbody>
    </table>
{% endblock %}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  
Using a `simple_tag` is important in this stage, as a normal filter can only
accept one argument, and in our case we want to pass in both the user and the
magazine as arguments. Don’t forget to create your \__init__.py file in the
templatetags directory!

At this point, it’s a good idea to create migrations and then run them so we can
enable our new models and include the transaction tracking from Django-Paypal.

We’ll also need to add our Magazine and Purchase models to our
magazines/admin.py:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.contrib import admin
from .models import Magazine
from .models import Purchase
 
admin.site.register(Magazine)
admin.site.register(Purchase)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now go ahead and create some magazines using the admin panel.
