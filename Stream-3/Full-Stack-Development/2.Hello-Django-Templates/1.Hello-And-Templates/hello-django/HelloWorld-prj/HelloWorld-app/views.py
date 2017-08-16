# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def say_hello(request):
	name = "Bootcamper"
	html = "<html><body><h1>Hello %s!</h1></body></html>" % name
	return HttpResponse(html)
