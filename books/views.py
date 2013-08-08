# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from books.models import *
from django.template import RequestContext, loader
from django.shortcuts import redirect
from django.contrib.auth import logout,login, authenticate
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
import random
import json
import pytranslate

def index(request):
    try:
        quotes = Quote.objects.all()
    except:
        user = User()
        book = Book(user = user, title = 'The perks of being walflower', author = 'Steven Chobsky')
        quotes = [Quote(book = book, user = user, text = 'Right now we are alive and in this moment I swear we are infinite.')]
    finally:
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

@login_required
def books(request):
    books = Book.objects.filter(user = request.user.id)
    temp = loader.get_template('books.html')
    context = RequestContext(request, {
        'books': books,
    })
    return HttpResponse(temp.render(context))

@login_required    
def book_id(request, id_num):
    book = Book.objects.get(id = int(id_num))
    page = 1
    temp = loader.get_template('book.html')
    context = RequestContext(request, {
          'book': book,
          'page': page,
    })
    return HttpResponse(temp.render(context))

@login_required
def book_id_page(request, id_num, page_num):
    book = Book.objects.get(id = int(id_num))
    page = int(page_num)
    temp = loader.get_template('book.html')
    context = RequestContext(request, {
          'book': book,
          'page': page,
    })
    return HttpResponse(temp.render(context))

def quotes(request):
    quotes = Quote.objects.filter(user = request.user.id)
    temp = loader.get_template('quotes.html')
    context = RequestContext(request, {
        'quotes': quotes,
    })
    return HttpResponse(temp.render(context))

def quote(request):
    user = User.objects.get(id = request.user.id)
    book = Book.objects.get(id = request.POST['book_id'])
    text = request.POST['quote_text']
    quote = Quote(user = user, book = book, text = text) 
    quote.save()
    response = {'success': True}
    return HttpResponse(json.dumps(response), content_type="application/json") 

def reviews(request):
    reviews = Review.objects.filter(user = request.user.id)
    temp = loader.get_template('reviews.html')
    context = RequestContext(request, {
            'reviews': reviews,
    })
    return HttpResponse(temp.render(context))

def review(request):
    user = User.objects.get(id = request.user.id)
    book = Book.objects.get(id = request.POST['book_id'])
    text = request.POST['text']
    review = Review(user = user, book = book, text = text)
    review.save()
    response = {'success': True }
    return HttpResponse(json.dumps(response), content_type='application/json')    

def translate(request):
    translation = pytranslate.translate(request.POST['text'], sl = 'english', tl = 'bulgarian')
    response = {'text': translation }
    return HttpResponse(json.dumps(response), conten_type = 'application/json')
     
def upload(request):
    if request.method == 'GET':
        temp = loader.get_template('upload.html')
        context = RequestContext(request, {
                'session': request.session,
        })
        return HttpResponse(temp.render(context))
    elif request.method == 'POST':
        text = request.FILES['book'].read()
        user = User.objects.get(id = request.user.id)
        book = Book(user = user, text = text, author = request.POST['author'], title = request.POST['title'])
        book.save()
        return HttpResponseRedirect('/books')
