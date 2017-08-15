# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from ModelTest_app.models import Contact


# Create your views here.
def get_contacts(request):
    return render(request, "ModelTest/home.html", {'contact_list': Contact.objects.all()})
