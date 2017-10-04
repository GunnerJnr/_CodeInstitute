# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Two sequence containing different possible
# states of a Todo item..
STATUS_CHOICES = (
    ('1', 'Todo'),
    ('2', 'Doing'),
    ('3', 'Done'),
)


class Todo(models.Model):
    """
    Todo Model:

    Contains the 'title', 'description', 'status' & 'updated' fields
    for a Todo item
    """
    title = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=255, null=False)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    updated = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return self.title
