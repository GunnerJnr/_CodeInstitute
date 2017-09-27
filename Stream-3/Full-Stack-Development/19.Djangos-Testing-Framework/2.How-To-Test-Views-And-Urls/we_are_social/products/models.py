# -*- coding: utf-8 -*-
"""
The models file for creating models for the products app
"""
from __future__ import unicode_literals

import uuid

from django.conf import settings
from django.db import models
from paypal.standard.forms import PayPalPaymentsForm


# Create your models here.
class Product(models.Model):
    """
    name: the name of the item
    description: the item's description
    price: the price of the item
    """
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    @property
    def paypal_form(self):
        """
        business: the email address of our merchant
        amount: the price of our production
        currency: USD in our case!
        item_name: the item’s … name!
        Invoice: A string to uniquely identify our transaction. In our case, we’re combining
        the primary key value of our product and a randomly generated unique id
        notify_url: where PayPal can send any success or error messages on our site
        return_url: where to return a customer after the payment process is complete
        cancel_url: where to return the customer if they choose to cancel the payment process
        """
        paypal_dict = {
            "business": settings.PAYPAL_RECEIVER_EMAIL,
            "amount": self.price,
            "currency": "USD",
            "item_name": self.name,
            "invoice": "%s-%s" % (self.pk, uuid.uuid4()),
            "notify_url": settings.PAYPAL_NOTIFY_URL,
            "return_url": "%s/paypal-return" % settings.SITE_URL,
            "cancel_return": "%s/paypal-cancel" % settings.SITE_URL,
        }

        return PayPalPaymentsForm(initial=paypal_dict)

    def __unicode__(self):
        return self.name
