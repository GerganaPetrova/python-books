from django.db import models
from django.contrib.auth.models import User as BaseUser

class User(BaseUser):
    pass

class Book(models.Model):
    user = models.ForeignKey('User')
    text = models.TextField()
    author = models.CharField(max_length = 50)
    title = models.CharField(max_length = 100)

    @property
    def pages(self):
        page_length = 25
        lines = self.text.split('\n')
        return [lines[i:i+page_length] for i in range(0, len(lines), page_length)]    

class Quote(models.Model):
    book = models.ForeignKey('Book')
    user = models.ForeignKey('User')
    text = models.CharField(max_length = 100)

class Review(models.Model):
    book = models.ForeignKey('Book')
    user = models.ForeignKey('User')
    text = models.TextField()    
