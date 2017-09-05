### USE DJANGO ORM TO CONNECT USERS TO THEIR PURCHASES

As explained before, we’ll be responding to *Signals* sent through the framework
to our code when certain events are triggered from the Django-Paypal system.

In order to keep our logic separate, we’ll create a new file in our magazines
app called signals.py and we’ll add the following:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import arrow
from .models import Purchase
 
 
def subscription_created(sender, **kwargs):
 
    ipn_obj = sender
    magazine_id = ipn_obj.custom.split('-')[0]
    user_id = ipn_obj.custom.split('-')[1]
    Purchase.objects.create(magazine_id=magazine_id,
                            user_id=user_id,
                            subscription_end=arrow.now().replace(weeks=+4).datetime)
 
 
def subscription_was_cancelled(sender, **kwargs):
 
    ipn_obj = sender
    magazine_id = ipn_obj.custom.split('-')[0]
    user_id = ipn_obj.custom.split('-')[1]
    purchase = Purchase.object.get(user_id=user_id, magazine_id=magazine_id)
    purchase.subscription_end = arrow.now().datetime
    purchase.save()
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To ensure that signals fire correctly, we’ll add this to the end of
the **magazines/models.py** file:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
...
from signals import subscription_created, subscription_was_cancelled
from paypal.standard.ipn.signals import valid_ipn_received
 
valid_ipn_received.connect(subscription_created)
valid_ipn_received.connect(subscription_was_cancelled)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In here, we define two functions to handle what happens when
the `subscription_signup` and `subscription_cancel` signals are sent.

We use the `connect()` method on these signals to tell Django that we want this
code to be run whenever those signals are sent.

So in the function `subscription_created`, we have a ‘sender’ argument sent with
the signal, and in our case, this is actually an instance of the instant payment
notification. So we simply rename the sender to `ipn_obj` for the sake of making
it more understandable.

 

### NOTE<br>Sometimes it may take a while before the signals get fired. This is because Paypal might not call the NOTIFY_URL immediately.

 

Next, we take our ‘custom’ attribute that we defined earlier in our
PayPalPaymentForm and split the string to gain our two ids for our user and
magazine.

We can now create a purchase record linking our user to the magazine and setting
the `subscription_end` to 4 weeks from now, using the excellent arrow module we
were introduced to back in our Stripe units.

In our cancelling function though, we are doing the same but then setting
the `subscription_end` value to `arrow.now()`, which effectively ends the
subscription right away. You might not want to be so harsh in practice, however.
Customers can get upset pretty quickly!
