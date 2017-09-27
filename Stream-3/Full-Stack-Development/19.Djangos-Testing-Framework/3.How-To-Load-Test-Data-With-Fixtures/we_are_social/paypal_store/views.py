# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def paypal_return(request):
    args = {'post': request.POST, 'get': request.GET}
    return render(request, 'paypal/paypal_return.html', args)


def paypal_cancel(request):
    args = {'post': request.POST, 'get': request.GET}
    return render(request, 'paypal/paypal_cancel.html', args)
