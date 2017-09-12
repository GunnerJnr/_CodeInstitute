# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from django.utils import timezone
from tinymce.models import HTMLField


# Create your models here.
class Subject(models.Model):
    """
    name:
    description: is a new field that comes packaged with
    django-tinymce. It enables our field to render the WYSIWYG editor
    in our admin
    """
    name = models.CharField(max_length=255)
    description = HTMLField()

    def __unicode__(self):
        return self.name


class Thread(models.Model):
    """
    name:
    user:
    subject: the thread subject
    created_at: record the time the posts and threads are created
    """
    name = models.CharField(max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='threads')
    subject = models.ForeignKey(Subject, related_name='threads')
    created_at = models.DateTimeField(default=timezone.now)


class Post(models.Model):
    """
    thread:
    comment:
    user: link back tot he user who created the post
    created_at: record the time the posts and threads are created
    """
    thread = models.ForeignKey(Thread, related_name='posts')
    comment = HTMLField(blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='posts')
    created_at = models.DateTimeField(default=timezone.now)
