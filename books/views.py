# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from books.models import *
from django.template import RequestContext, loader
from django.shortcuts import redirect
from django.contrib.auth import logout,login, authenticate
from django.contrib.auth.decorators import login_required
import random

def index(request):
    quotes = Quote.objects.all()
    temp = loader.get_template('index.html')
    context = RequestContext(request, {
            'quote': random.choice(quotes),
            'session': request.session,
    })
    return HttpResponse(temp.render(context))

def my_login(request):
    if request.method == 'GET':
        temp = loader.get_template('login.html')
        context = RequestContext(request, {
                'sesstion': request.session,
        })
        return HttpResponse(temp.render(context))
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/index')
        else:
            return HttpResponseRedirect('/login')    

def logout(request):
    logout(request)
    return HttpResponeRedirect('/index')

def signup(request):
    if request.method == 'GET':
        temp = loader.get_template('signup.html')
        return HttpResponse(temp.render())
    elif request.method == 'POST':
        user = User(request)

