Custom User Model
=================

##### In this unit the students learn how to override Django's default User model to create their own custom user model

 

### CUSTOM USER MODEL

We need a custom user model, which will contain our new way of logging in. This
will be implemented in the ‘accounts’ app you created earlier.

### DERIVE THE NEW USER MODEL – IMPORT DEPENDENCIES

Add the imports you need to the models.py in the accounts app:

 

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.utils import timezone
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We now have a place to start when deriving our new model from
the *AbstractUser*, which contains a basic set of attributes for our User model
that will be compatible with Django’s needs.

Django will need attributes like *is_superuser* and *is_active*, so that any
users created will have a default set of permissions for the admin, for
instance.

The other interesting thing we’ve imported is *UserManager*, which is the class
that you access when you type *User.objects*. That object’s property is actually
an instance of the UserManager class, and handles things like
creating *normal* and *superuser* accounts when you register someone new.

We’ll be customising this later though, so it’s a good idea to import it now.

Now we can write the code for our new user class and configure Django to start
using that to record our user activity:

 

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class AccountUserManager(UserManager):
    def _create_user(self, username, email, password,
                     is_staff, is_superuser, **extra_fields):
        """
       Creates and saves a User with the given username, email and password.
       """
        now = timezone.now()
        if not email:
            raise ValueError('The given username must be set')
 
        email = self.normalize_email(email)
        user = self.model(username=email, email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
 
        return user
 
class User(AbstractUser):
    # now that we've abstracted this class we can add any
    # number of custom attribute to our user class
 
    # in later units we'll be adding things like payment details!
 
    objects = AccountUserManager()
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In our *User* class, we replace the *objects* property with our custom
AccountUserManager, which uses all the normal functions of the UserManager but
overrides the \_create_user method so that we can do a simple check that the
supplied email is correct.

This is almost exactly as the the default manager, but the default version
checks for a username. In our case, we’re not going to use username as the main
piece of login information, so we do need to make that check match our goals.

Notice also that we’re passing ‘username=email’ here. That’s because we are not
going to be passing any username. The field can’t be blank, however, and must
also be unique.

To tell Django that we want to use this class as our User class, we need to add
a line to the settings.py:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
AUTH_USER_MODEL = 'accounts.User'
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When Django starts up, it will check for the AUTH_USER_MODEL setting. If it
finds it, it will use that definition of the class instead of the built-in
version that you might have come across before.
