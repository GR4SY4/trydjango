# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def product_view(request, *args, **kwargs):
	print(args, kwargs)
	print(request.user)
	return render(request, "product.html", {})

def checkout_view(request, *args, **kwargs):
	print(args, kwargs)
	print(request.user)
	return render(request, "checkout.html", {})

def cart_view(request, *args, **kwargs):
	print(args, kwargs)
	print(request.user)
	return render(request, "cart.html", {})

def categories_view(request, *args, **kwargs):
	print(args, kwargs)
	print(request.user)
	return render(request, "categories.html", {})

