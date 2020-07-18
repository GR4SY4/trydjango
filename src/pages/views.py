# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
	print(args, kwargs)
	print(request.user)
	return render(request, "index.html", {})

def login_view(request, *args, **kwargs):
	print(args, kwargs)
	print(request.user)
	return render(request, "login.html", {})

def register_view(request, *args, **kwargs):
	print(args, kwargs)
	print(request.user)
	return render(request, "register.html", {})

def contact_view(request, *args, **kwargs):
	print(args, kwargs)
	print(request.user)
	return render(request, "contact.html", {})