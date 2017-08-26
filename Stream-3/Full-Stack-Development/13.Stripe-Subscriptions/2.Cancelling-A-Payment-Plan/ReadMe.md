###  

Cancelling a Payment Plan
=========================

##### In this unit the students will learn how to cancel a Stripe payment plan in their Django site

 

### CANCELLING A PAYMENT PLAN

Once our user is registered and setup, we’ll need to provide a method
for cancelling the subscription in accordance with Stripe’s guidelines.

So we first need to create a view in our accounts app that we will use from our
users profile page:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@login_required(login_url='/accounts/login/')
def cancel_subscription(request):
   try:
       customer = stripe.Customer.retrieve(request.user.stripe_id)
       customer.cancel_subscription(at_period_end=True)
   except Exception, e:
       messages.error(request, e)
   return redirect('profile')
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The first task at hand here is to get an instance of the Stripe customer from
Stripe. To do that, we access the user object that’s now being passed in
the *request* object passed as the argument to the *cancel_subscription()*. The
request object represents contains the details of the currently logged
in *user*.

From that user, we get our stripe_id too, which should now be the stripe
customer string that we saved during registration.

We pass the strip_id value as an argument to *stripe.Customer.retrieve()* to get
our stripe customer via the stripe API.

If that method call succeeds, we then have an instance of the Stripe customer
that calls the *cancel_subscription()* method to close off the account’s payment
plan.

   
At this point, you could choose to stop the subscription right away, but in our
case, we’re going to be kind and allow them to use the service until the billing
period has ended.

If we did want to end the subscription now, we could have used *arrow* to set
the subscription_end field on our user to ‘arrow.now()’.

Once we have the cancellation functionality in place, we need a location to fire
off a cancellation event. A good place to do this is on our profile page. So
let’s do that now:

**Line 7:** We let the user know how much time is left on the subscription – to
do this we access the user.subscription_end field that we just added to the User
model. We also use a handy template tag called *timeuntil* that works out the
time from now until the subscription end and presents it in a user friendly
format (similar to the functionality that *arrow* provides).

**Lines 10-12:** We include a styled link that redirects to
a *cancel_subscription* url in order to invoke the *cancel_subscription* view
that we created earlier. The lnk also calls to cancelSubscriptionCheck() when
the onclick event is fired.

**Lines 14-21:** *cancelSubscriptionCheck()* contains a simple piece of code
that pops up a confirmation message box that ensures that the user has made an
active choice to cancel. Only when the user confirms will the link actively
redirect to our url.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
{% extends "base.html" %}
{% block content %}
    <h2>Success!</h2>
    <p>You are logged in as {{ user.email }} </p>
    <p>Your stripe id is {{ user.stripe_id }} </p>
    <h2>Subscription Details</h2>
    <p>You have {{ user.subscription_end|timeuntil}} left on your subscription</p>
    <p>To cancel your subscription click 'Cancel Subscription' below</p>
    <p>
        <a href="{% url "cancel_subscription" %}"
           onclick="return cancelSubscriptionCheck();"
           class="btn btn-danger">Cancel Subscription</a>
    </p>
    <script type="text/javascript">
        function cancelSubscriptionCheck() {
            if (confirm('Are you sure you want to cancel?')) {
                return true;
            }
            return false;
        }
    </script>
{% endblock %}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Don’t forget to update *urls.py* with the expected url pattern:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
url(r'^cancel_subscription/$', accounts_views.cancel_subscription, name='cancel_subscription'),
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Also we need to be able to navigate to our profile page once we are logged in.
So let’s update our *base.html* page to include a link to profile:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
<ul class="nav nav-pills pull-right">
            <li><a href="/">Home</a></li>
            <li><a href="/pages/about/">About</a></li>
            <li><a href="#">Contact</a></li>
            {% if user.is_authenticated %}
                <li><a href="{% url 'profile' %}">Profile</a></li>
                <li><a href="{% url 'logout' %}">Log Out</a></li>
            {% else %}
                <li><a href="{% url 'register' %}">Register</a></li>
                <li><a href="{% url 'login' %}">Log In</a></li>
            {% endif %}
        </ul>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Your profile page should now look something like below:

![](http://codeinstitute.wpengine.com/wp-content/uploads/2016/01/stripesubscription1.png)
