### SETUP DJANGO FOR SUBSCRIPTION HANDLING

As usual, we need to make some configuration changes to Django so we can enable
the functionality we need for subscriptions.

Previously we only used the Django-Paypal API to create some *Buy Now* buttons.
There is, however, a whole backend to Django-Paypal that handles transaction
tracking, and we’re going to enable that to allow us to connect
to *Signals* that are sent through the Django framework.

### DJANGO SIGNALS

Part of the framework in Django sends messages (‘Signals’) to other parts of the
system when certain events happen.

In our case, we’re going to be listening out for subscription events that will
tell us that the subscription was either created or cancelled.

More on this later in the unit …

### SETTINGS

In our settings.py, we need to include the backend for Django-Paypal to enable
the tracking:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
INSTALLED_APPS = [
    ...
    'paypal.standard.ipn',
]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We won’t be running `python manage.py migrate` just yet though, as we have some
more changes to make.
