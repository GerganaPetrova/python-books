# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from books.models import *
from django.template import RequestContext, loader
from django.shortcuts import redirect
from django.contrib.auth import logout,login, authenticate
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
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
                'session': request.session,
        })
        return HttpResponse(temp.render(context))
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            temp = loader.get_template('index.html')
            context = RequestContext(request, {
                    'user': user,
            })
            return HttpResponse(temp.render(context))
        else:
            return HttpResponseRedirect('/login')    

def my_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def signup(request):
    if request.method == 'GET':
        temp = loader.get_template('signup.html')
        context = RequestContext(request, {
                'session': request.session,
        })
        return HttpResponse(temp.render(context))
    elif request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        user = User(first_name = first_name, last_name = last_name, email = email, username = username)
        user.set_password(password)
        user.save()
        send_mail("Wellcome %s" % user.get_full_name(),"Hello, dumbass!", 'example.online.reader@gmail.com',[email])
        return HttpResponseRedirect('/login')

