from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Context, loader
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from . import models

def index(request):
    
    # Deals with getting the context
    context = {}
    if request.user.is_authenticated():
        messageQS = models.Message.objects.filter(recipient=request.user).order_by('-id')
        context['messages'] = messageQS
    
    # if get request
    if request.method == "GET":
        return render(request, 'MyApp/index.html', context)

    # if post request
    elif request.method == "POST":
        message = request.POST['message']
        recipient_name = request.POST['recipient']
        sender = request.user

        try:
            recip_user = User.objects.get(username = recipient_name)
        except:
            #print("Something went wrong... invalid username")
            context['note'] = "User does not exist"
            return render(request, 'MyApp/index.html', context)

        models.Message.objects.create(
            message=message,
            recipient=recip_user,
            sender=sender
        )

        return redirect('/')


def submit_login(request):
    context = {}
    if request.method == "GET":
        return render(request, 'MyApp/login.html', {})
    
    elif request.method == "POST":
        try:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)

            if user is not None:    
                login(request, user)
                return redirect('/') 
            else:
                context['note'] = "Wrong username/password"
                return render(request, 'MyApp/login.html', context)
                
        except:
            print('Error logging in')
            return redirect('/')

def submit_logout(request):
    logout(request)
    return redirect('/')