# Create your views here.
from django.http import HttpResponse
import books.models
from django.templates import Context, loader
from django.shortcuts import redirect
from django.contrib.auth import logout,login, authenticate
from django.contrib.auth.decorators import login_required

def my_index(request):
    quotes = Quote.objects.all()
    temp = loader.get_template('/templates/index.html')
    context = Context({
            'all_quotes': quotes
    })
    return HttpResponse(temp.render(context))

def login(request):
    if request.method == 'GET':
        temp = loader.get_template('/templates/login.html')
        return HttpResponse(temp.render())
    elif request.method = 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            if user.is_active():
                login(request, user)
                return redirect('my_index')
            else:
                 return redirect('login')    

def logout(request):
    logout(request)
    return redirect('my_index')

def signup(request):
    if request.method == 'GET':
        temp = loader.get_template('/templates/signup.html')
        return HttpResponse(temp.render())
    elif request.method == 'POST':
        user = User(request)

