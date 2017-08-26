###  

### SETTING UP A MONTHLY PAYMENT PLAN IN STRIPE

Creating a subscription payment plan in Stripe is a two-step process.

First, we need to create the details of the actual payment plan within our
Stripe user account:

![](http://codeinstitute.wpengine.com/wp-content/uploads/2016/01/1452104894_image2.png)

In our accounts dashboard, we click ‘Plans’, then ‘Create you first plan’.

![](http://codeinstitute.wpengine.com/wp-content/uploads/2016/01/1452104894_image3.png)

We need to add in a string to later identify the plan in our code, so we’ve
entered ‘REG_MONTHLY’ here.

The other details are pretty much self explanatory – except for *Statement
desc*, which is actually how this will display on the customer’s bank statement.

Once you’re finished, click ‘Create plan’ and you’re done! You should now see
the new plan listed in the ‘Plans’ pane.

 

### CREATING A SUBSCRIPTION IN CODE

To create a subscription, we need to alter our single payment code from the
previous unit to setup the subscription instead.

Also, because we are handling subscriptions, it’s a good idea to replace the
card/token/id with our customer’s once we have used it, as this will be more
useful when updating or cancelling our customer’s subscription.

Let’s take a look at the new method of setting up the subscription:

Open your previously created stripe basic payments project.

Modify the *register()* function in *accounts.views* as per below:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
...  
                customer = stripe.Customer.create(
                    email=form.cleaned_data['email'],
                    card=form.cleaned_data['stripe_id'], # this is currently the card token/id
                    plan='REG_MONTHLY',
                )
...
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Instead of creating a charge, this time we create a customer object within
Stripe using the email and Stripe token/id. Also, we pass the name of our newly
created plan to tell Stripe which one we’re subscribing our new user to. While
still in the *register()* function make the following edits.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
...  
 
                if customer:
                    user = form.save()
                    user.stripe_id = customer.id
                    user.subscription_end = arrow.now().replace(weeks=+4).datetime
                    user.save()
...
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Next, we save our new user and replace the `stripe_id` value with the customer
id that Stripe will supply in the customer object (it will be a string of the
form ‘cus_XXXXXXXXXXXXXX’). Why? Because later in the unit, we’ll use this in
updating our user’s subscription and also in the cancelling process.

You could in practice store both, of course, but we’re only interested in
keeping tabs on the subscription and won’t be taking any one-off payments later,
so there’s no need to retain that data.

Before saving the user again, we also make use of the excellent *arrow*, which
can be installed by ‘pip install arrow’ or ‘easy_install arrow’.

*arrow* is a fast and simple way of dealing with dates and times in Python.
It will be very useful to us in tracking our user’s subscription periods.
Install arrow via pip or else via the Pycharm settings dialog . Then import
arrow at the top of *accounts/views.py*.

In our case, we’re creating a date that is exactly 4 weeks from now and
converting it into a datetime object which is compatible with our DateTimeField
that we need to add to our *User*model:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class User(AbstractUser):
    stripe_id = models.CharField(max_length=40, default='')
    subscription_end = models.DateTimeField(default=timezone.now)
    objects = AccountUserManager()
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After remembering to create and run the migrations, we can then use this to know
when the user’s subscription is over.
