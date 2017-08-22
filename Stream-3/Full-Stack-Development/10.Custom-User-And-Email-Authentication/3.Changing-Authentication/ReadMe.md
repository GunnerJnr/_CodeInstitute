Changing Authentication
=======================

##### In this unit the students will learn how to customise Django's authentication mechanism

 

### CHANGING AUTHENTICATION

‘Out of the box’ Django prefers to confirm the identity of a user by checking
the username and password fields of the User model, but we want to do something
a little different to show you that there is the possibility of using
alternative ways to authenticate your users.

In this section, we’re going to add some code to make Django use the email field
instead!

Firstly, we’ll need to add a file to the ‘accounts’ app called *backends.py*.  


![](https://lms.codeinstitute.net/wp-content/uploads/2016/01/1451948610_image2-1.png)

  
This file will hold our code to check if the email and password are correct, and
also to allow/disallow login:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from models import User
 
class EmailAuth(object):
 
    def authenticate(self, email=None, password=None):
        """
       Get an instance of User using the supplied email and check its password
       """
        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                return user
 
        except User.DoesNotExist:
            return None
 
    def get_user(self, user_id):
        """
       Used by the django authentication system to retrieve an instance of User
       """
        try:
            user = User.objects.get(pk=user_id)
            if user.is_active:
                return user
            return None
        except User.DoesNotExist:
            return None
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Here we’ve created a class that will replace the standard ‘auth’ object that
Django uses to check logins, and we override two of its default methods.

The authenticate method is where we are doing the main logic by finding the user
by the email address and then checking password.

This is actually not that different from the default method for testing against
the username field. We’ve simply swapped out the username field for the email
field.

However, most websites these days at least require an email to let you into
their sites so that you can handle lost passwords and update users via email.
Thus, this method is far more useful in the real world.

Lastly, you can see that we have overridden the get_user method to show that you
can apply extra conditions to the login process! In this case, we’re simply
making sure a user is active and whether they can log in.

This is ideal for a user ban or disabling accounts that haven’t been used for a
long time, for example, so it’s worth knowing how simple this is to implement in
Django!

### SETTING THE BACKEND

At this point, we need to modify our settings.py so that Django knows to use
this backend instead of the system default:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'accounts.backends.EmailAuth',
)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Again, Django will check when the server runs and re-route all calls to the
‘auth’ object to our newly defined authentication class.
