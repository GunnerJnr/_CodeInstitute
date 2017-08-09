# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def show_home(request):
    return render(request, "home.html", {"home_page": "Welcome to the Django 'Home' page"})


def show_about(request):
    return render(request, "about.html", {"about_page": "Welcome to the Django 'About Us' page"})


def show_contact(request):
    return render(request, "contact.html", {"contact_page": "Welcome to the Django 'Contact Us' page"})

