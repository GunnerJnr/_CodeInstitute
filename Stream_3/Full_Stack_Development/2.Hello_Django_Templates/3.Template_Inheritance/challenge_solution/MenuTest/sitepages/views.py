# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
import datetime


# Create your views here.
def show_home(request):
    current_day = datetime.date.today().strftime("%A")
    current_date = datetime.date.today()
    return render(request, "home.html", {
        "home_page": "Welcome to the Django 'Home' page",
        "day_of_week": current_day,
        "date_today": current_date
    })


def show_about(request):
    return render(request, "about.html", {
        "about_page": "Welcome to the Django 'About Us' page",
        "site_description": "This site is dedicated to bringing you the latest technologies and web frameworks that we"
        "think will be the future contenders in development. NASA has challenged designers to develop a conventional "
        "drone to work inside a space station, navigating with no ‘up’ or ‘down’. The winning design, ArachnoBeeA,"
        "would use cameras and tiny beacons to manoeuvre its way around. How popular drones would be in such a "
        "confined space is a different question"
        "This site is dedicated to bringing you the latest technologies and web frameworks that we"
        "think will be the future contenders in development. NASA has challenged designers to develop a conventional "
        "drone to work inside a space station, navigating with no ‘up’ or ‘down’. The winning design, ArachnoBeeA,"
        "would use cameras and tiny beacons to manoeuvre its way around. How popular drones would be in such a "
        "confined space is a different question"
        "This site is dedicated to bringing you the latest technologies and web frameworks that we"
        "think will be the future contenders in development. NASA has challenged designers to develop a conventional "
        "drone to work inside a space station, navigating with no ‘up’ or ‘down’. The winning design, ArachnoBeeA,"
        "would use cameras and tiny beacons to manoeuvre its way around. How popular drones would be in such a "
        "confined space is a different question"
    })


def show_contact(request):
    return render(request, "contact.html",{
        "contact_page": "Welcome to the Django 'Contact Us' page",
        "full_name": "David Gunner",
        "role_title": "Student @ Code Institute",
        "telephone": "01234 567890",
        "email": "gunnerjnr@live.co.uk",
        "button_text": "Send Email"
    })
