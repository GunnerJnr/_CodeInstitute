# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def say_hello(request):
	name = "Bootcamper"
	html = "<html><body><h1>Hello %s!</h1></body></html>" % name
	return HttpResponse(html)

def get_now(request):
	now = datetime.datetime.now()
	return render(request, "HelloWorld/base.html", {"current_date": now})

def inheritance_test(request):
	return render(request, "HelloWorld/home.html",
		{"a_variable": "I've been rendered in the child template",
		"another_variable": "Me too!"})