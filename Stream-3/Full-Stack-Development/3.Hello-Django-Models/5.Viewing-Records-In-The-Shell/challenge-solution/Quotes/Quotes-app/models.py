# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Quotes(models.Model):

    class Meta:  # include this to ensure build in IDE
        app_label = "Quotes_app"

    quoter_first_name = models.CharField(max_length=255)
    quoter_last_name = models.CharField(max_length=255)
    quote_text = models.CharField(max_length=255)

    def __str__(self):
        return ' '.join([
            self.quoter_first_name,
            self.quoter_last_name,
        ])
