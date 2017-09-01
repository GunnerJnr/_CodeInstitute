# -*- coding: utf-8 -*-
"""
The model file for creating classes to be used with our
magazines app.
"""
from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from django.utils import timezone


# Create your models here.
# Create the Magazine class
class Magazine(models.Model):
    """
    name: the name of the item
    description: the item's description
    price: the monthly subscription price
    """
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __unicode__(self):
        return self.name


class Purchase(models.Model):
    """
    user:
    magazine:
    subscription_end:
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='purchases')
    magazine = models.ForeignKey(Magazine)
    subscription_end = models.DateTimeField(default=timezone.now)
