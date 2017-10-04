# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request, 'MyApp/index.html', {})

def submit_login(request):
	return render(request, 'MyApp/index.html', {})

def submit_logout(request):
	return render(request, 'MyApp/index.html', {})
