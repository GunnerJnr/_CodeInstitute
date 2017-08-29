# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils import timezone


# Create your models here.
# Create our new user class
class AccountUserManager(UserManager):
    def _create_user(self, username, email, password, is_staff, is_supervisor, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        :param username:
        :param email:
        :param password:
        :param is_staff:
        :param is_supervisor:
        :param extra_fields:
        :return:
        """
        now = timezone.now()
        if not email:
            raise ValueError('The given username must be set')

        email = self.normalize_email(email)
        user = self.model(username=email, email=email, is_staff=is_staff, is_active=True,
                          is_supervisor=is_supervisor, date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)

        return user


# now that we've abstracted this class we can add any
# number of custom attribute to our user class
class User(AbstractUser):
    # store our stripe token/id for later use
    stripe_id = models.CharField(max_length=40, default='')

    # in later units we'll be adding things like payment details!
    objects = AccountUserManager()