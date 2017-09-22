# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Product


# Create your views here.
@login_required(login_url='/login/')
def all_products(request):
    products = Product.objects.all()
    return render(request, "products/products.html", {"products": products})
