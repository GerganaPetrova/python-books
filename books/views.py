# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from books.models import *
from django.template import RequestContext, loader
from django.shortcuts import redirect, render
from django.contrib.auth import logout,login, authenticate
from django.core.mail import send_mail
import random
import json
from django.views.generic.base import View
from django.views.generic import ListView

class Index(View):
    template_name = 'index.html'

    def get(self, request):
        try:
            quotes = Quote.objects.all()
            quote = random.choice(quotes)
        except:
            user = User()
            book = Book(user = user, title = 'The perks of being walflower', author = 'Steven Chobsky')
            quotes = [Quote(book = book, user = user, text = 'Right now we are alive and in this moment I swear we are infinite.')]
            quote = random.choice(quotes)
        finally:
            return render(request, self.template_name, {'quote': quote})

class LoginView(View):
    template_name = 'login.html'

    def get(self,request):
        return render(request, self.template_name)        

    def post(self, request, *args, **kwargs):
        user = authenticate(username = request.POST['username'], password = request.POST['password'])
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/login')

class LogoutView(View):
    template_name = 'logout.html'

    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')

class Signup(View):
    template_name =  'signup.html'
    
    def get(self, request):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
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

class Books(ListView):
    model = Book
    template_name = 'books.html'
    
    def get_queryset(self):
        queryset = Book.objects.filter(user = self.request.user.id)
        return queryset

class BookId(View):
    template_name = 'book.html'

    def get(self, request, *args, **kwargs):
        book = Book.objects.get(**kwargs)
        page = 1
        return render(request, self.template_name,{ 'book': book,
                                                    'page': '\n'.join(book.pages(page)),
                                                    'page_previous': 1,
                                                    'page_next': 2,
                                                  }) 
class BookIdOnPage(View):
    template_name = 'book.html'

    def get(self,request, *args, **kwargs):
        book = Book.objects.get(id = kwargs['id'])
        page_num = int(kwargs['page_num'])
        return render(request, self.template_name,{ 'book': book,
                                                    'page_previous': page_num - 1,         
                                                    'page_next': page_num + 1,
                                                    'page': '\n'.join(book.pages(page_num)),
                                                  })

class QuotesView(ListView):
    model = Quote 
    template_name = 'quotes.html'
    
    def get_queryset(self):
        queryset = Quote.objects.filter(user = self.request.user.id)
        return queryset

class QuoteView(View):
    
    def post(self, request):
        user = User.objects.get(id = request.user.id)
        book = Book.objects.get(id = request.POST['book_id'])
        text = request.POST['quote_text']
        quote = Quote(user = user, book = book, text = text) 
        quote.save()
        response = {'success': True}
        return HttpResponse(json.dumps(response), content_type="application/json") 

class ReviewsView(View):
    template_name = 'reviews.html'

    def get(self, request):
        reviews = Review.objects.filter(user = request.user.id)
        return render(request, self.template_name, { 'reviews': reviews })

class ReviewView(View):
    
    def post(self, request):
        user = User.objects.get(id = request.user.id)
        book = Book.objects.get(id = request.POST['book_id'])
        text = request.POST['text']
        review = Review(user = user, book = book, text = text)
        review.save()
        response = {'success': True }
        return HttpResponse(json.dumps(response), content_type='application/json')    
     
class Upload(View):
    template_name = 'upload.html'

    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs):
        text = request.FILES['book'].read()
        user = User.objects.get(id = request.user.id)
        book = Book(user = user, text = text, author = request.POST['author'], title = request.POST['title'])
        book.save()
        return HttpResponseRedirect('/books')
