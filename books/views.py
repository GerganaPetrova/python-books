# Create your views here.
from django.http import HttpResponse
from books.models import *
from django.template import Context, loader
from django.shortcuts import redirect
from django.contrib.auth import logout,login, authenticate
from django.contrib.auth.decorators import login_required
import random

def index(request):
    quotes = Quote.objects.all()
    temp = loader.get_template('index.html')
    context = Context({
            'quote': random.choice(quotes),
            'session': request.session,
    })
    return HttpResponse(temp.render(context))

def my_login(request):
    if request.method == 'GET':
        temp = loader.get_template('login.html')
        return HttpResponse(temp.render())
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('index')
            else:
                 return redirect('my_login')    

def logout(request):
    logout(request)
    return redirect('index')

def signup(request):
    if request.method == 'GET':
        temp = loader.get_template('signup.html')
        return HttpResponse(temp.render())
    elif request.method == 'POST':
        user = User(request)

