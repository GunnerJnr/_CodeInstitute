###  

How to Test Models
==================

 

### HOW TO TEST MODELS

There isn’t much to testing models, as any functionality that a model might have
is generally derived from the basic building blocks in Django’s model framework.

That being said, the only things you might consider testing are those features
you have built onto the model that don’t come as standard to a Django model.

Perhaps you have a special method on there that generates something different?
In that case, you should consider making a test for it.

In our custom user model we created an alternative ModelManager for creating our
users; but to be honest, it’s only about two lines different from the original
UserManagers version. So perhaps the only test we could create would test to see
if those lines of code have changed in their operation:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class AccountUserManager(UserManager):
    def _create_user(self, username, email, password,
                     is_staff, is_superuser, **extra_fields):
        """
       Creates and saves a User with the given username, email and password.
       """
        now = timezone.now()
 
        # these lines here are different!
        if not email:
            raise ValueError('The given username must be set')
 
        # the rest is not!
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

And this really highlights another interesting idea – if you’re testing, you
should have a test for anything that has an if statement!

In this case, we should supply a set of data to `_create_user` that would cause
the ‘if not email’ clause to succeed and fail, to ensure it works in both
directions so to speak.

So for this case, our failure would be a ValueError exception that we can trap
in our test. In **accounts/test.py** add the following:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.test import TestCase
from .models import User
 
 
class CustomUserTest(TestCase):
 
    def test_manager_create(self):
        user = User.objects._create_user(None, "test@test.com",
                                         "password",
                                         False, False)
        self.assertIsNotNone(user)
 
        with self.assertRaises(ValueError):
            user = User.objects._create_user(None, None, "password",
                                             False, False)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In general, you shouldn’t really test your models unless they implement
something different from the standard features of Django’s models. After all,
Django have already tested their code, so why test it twice?
