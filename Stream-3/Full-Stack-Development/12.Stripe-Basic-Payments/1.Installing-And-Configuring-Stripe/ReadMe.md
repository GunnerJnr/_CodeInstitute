### INSTALLING AND CONFIGURING STRIPE

Staying within the project you created during custom user authentication, let’s
install Stripe.

Stripe comes as an installable module that you can add in
using *pip* or *easy_install*:

pip install stripe

Or

easy_install stripe

Once that’s done, we need to add a few lines to our settings.py so we can store
our Stripe authentication strings.  


### GETTING YOUR STRIPE AUTHENTICATION DETAILS

Before we can add those details, you’re going to need an actual account with
Stripe. So head over to [http://www.stripe.com](http://www.stripe.com/) and
complete the signup process. Once you’ve done that and you are able to login,
you should see your account settings in the small menu at the top right.

![](http://codeinstitute.wpengine.com/wp-content/uploads/2016/01/1452099024_image2.png)

  
Select this to go to your settings, where you can retrieve the authentication
details needed when making transaction requests.

![](http://codeinstitute.wpengine.com/wp-content/uploads/2016/01/1452099024_image3.png)

  
On the API Keys tab, you’ll find two sets of keys: test keys and live keys. The
ones we’re going to use here are the test keys. But when you go live with your
own projects, you simply swap these for the live versions in production code and
your transactions will be sent through the correct transaction handling systems.

Next, we simply cut and paste these values into the following code that you need
to add to your settings.py:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Stripe environment variables
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', '<replace this with your stripe publishable code>')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', '<replace this with your stripe secret code>')
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This then uses `os.getenv()` to search for the environment variables
STRIPE_PUBLISHABLE and STRIPE_SECRET on the production server (when the site is
live).

If they’re not found (if you’re running a local server, for example), it will
default to your test keys instead. 

 

### NOTE<br>Whilst environment variables are not covered here, it’s a great idea to leave things such as live authentication codes like this out of your code, and pick them up from the server they are run on.

 

That way, your code isn’t storing ‘hard coded’ information, and thus can be
deployed to any server. Besides, the server admin can take care of configuring
the server details.
