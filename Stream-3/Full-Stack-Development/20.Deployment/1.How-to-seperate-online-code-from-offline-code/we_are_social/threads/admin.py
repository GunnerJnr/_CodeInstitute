# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Post, Subject, Thread

# Register your models here.
admin.site.register(Subject)
admin.site.register(Thread)
admin.site.register(Post)
