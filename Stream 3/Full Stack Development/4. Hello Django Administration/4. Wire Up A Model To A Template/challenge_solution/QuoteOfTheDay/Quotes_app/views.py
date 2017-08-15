# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from Quotes_app.models import Quotes


# Create your views here.
def get_quotes(request):
    return render(request, "QuoteOfTheDay/home.html", {'quote_list': Quotes.objects.all()})
