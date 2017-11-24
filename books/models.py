from django.db import models
from unittest.util import _MAX_LENGTH

# Create your models here.

class Book(models.Model):
    book_title = models.CharField(max_length=200)
    volume_num = models.IntegerField(default=0)
    def __str__(self):
        return str(self.volume_num)+': '+self.book_title
    
class Author(models.Model):
    author_name = models.CharField(max_length=200)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    def __str__(self):
        return self.author_name
    
class Person(models.Model):
    firstname = models.CharField(max_length=200)
    lastname  = models.CharField(max_length=200)
    def __str__(self):
        return self.lastname+', '+self.firstname
    
class Edition(models.Model):
    year = models.IntegerField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    def __str__(self):
        return self.book.__str__()+'('+str(self.year)+')'
    
class Instance(models.Model):
    condition = models.CharField(max_length=64)
    price = models.FloatField(default=0.00)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    def __str__(self):
        return self.condition
    