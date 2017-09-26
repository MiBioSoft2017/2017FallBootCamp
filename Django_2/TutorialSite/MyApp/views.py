from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader

def index(request):
    return render(request, 'MyApp/index.html', {})

def submit_login(request):
    return render(request, 'MyApp/login.html', {})

def submit_logout(request):
    pass