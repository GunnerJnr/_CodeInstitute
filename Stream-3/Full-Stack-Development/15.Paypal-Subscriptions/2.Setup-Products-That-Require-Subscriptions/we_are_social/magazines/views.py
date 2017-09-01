# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Magazine


# Create your views here.
@login_required(login_url='/login/')
def all_magazines(request):
    magazines = Magazine.objects.all()
    return render(request, "magazines/magazines.html", {"magazines": magazines})
