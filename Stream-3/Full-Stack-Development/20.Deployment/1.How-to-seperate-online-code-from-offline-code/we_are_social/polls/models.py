# -*- coding: utf-8 -*-
from django.conf import settings
from django.db import models

from threads.models import Thread


# Create your models here.
class Poll(models.Model):
    question = models.TextField()
    thread = models.OneToOneField(Thread, null=True)

    def __unicode__(self):
        return self.question


class PollSubject(models.Model):
    name = models.CharField(max_length=255)
    poll = models.ForeignKey(Poll, related_name='subjects')

    def __unicode__(self):
        return self.name


class Vote(models.Model):
    poll = models.ForeignKey(Poll, related_name="votes")
    subject = models.ForeignKey(PollSubject, related_name="votes")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='votes')
