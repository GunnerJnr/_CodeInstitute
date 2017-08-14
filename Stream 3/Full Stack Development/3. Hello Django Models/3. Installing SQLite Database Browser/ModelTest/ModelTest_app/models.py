# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Contact(models.Model):

    class Meta:  # include this to ensure build in the IDE
        app_label = "ModelTest_app"

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    mobile_no = models.CharField(max_length=20)
