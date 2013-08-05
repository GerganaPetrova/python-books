from django.db import models

class Users(models.Model):
    name = models.CharField(max_length = 100)
    username = models.CharField(max_length = 20, unique = True)
    password = models.CharField(max_length = 20)
    e_mail = models.CharField(max_length = 100)

class Books(models.Model):
    user_id = models.ForeignKey('Users')
    text = models.TextField()
    author = models.CharField(max_length = 50)
    title = models.CharField(max_length = 100)

class Quotes(models.Model):
    book_id = models.ForeignKey('Books')
    user_id = models.ForeignKey('Users')
    text = models.CharField(max_length = 100)

class Reviews(models.Model):
    bookd_id = models.ForeignKey('Books')
    user_id = models.ForeignKey('Users')
    text = models.TextField()    
