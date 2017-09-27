# -*- coding: utf-8 -*-
"""
This is the models file for creating models for the accounts app
"""
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils import timezone


# Create your models here.
# Create our new user class
class AccountUserManager(UserManager):
    """
    Here we can create the class functions that will handle the user management
    """
    def _create_user(self, username, email, password, is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        :param username:
        :param email:
        :param password:
        :param is_staff:
        :param is_superuser:
        :param extra_fields:
        :return:
        """
        now = timezone.now()
        if not email:
            raise ValueError('The given username must be set')

        email = self.normalize_email(email)
        user = self.model(username=email, email=email, is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)

        return user


# now that we've abstracted this class we can add any
# number of custom attribute to our user class
class User(AbstractUser):
    """
    Here we create our own user class by using our overidden user class manager,
    this allows us to supply our own login rules, plus much more.
    """
    # store our stripe token/id for later use
    stripe_id = models.CharField(max_length=40, default='')
    # keep track of the time left on user subscription
    subscription_end = models.DateTimeField(default=timezone.now)
    objects = AccountUserManager()

    #
    def is_subscribed(self, magazine):
        """
        This function be responsible for checking if the user is subscribed
        """
        try:
            purchase = self.purchases.get(magazine__pk=magazine.pk)
        except Exception:
            return False

        if purchase.subscription_end > timezone.now():
            return False

        return True
