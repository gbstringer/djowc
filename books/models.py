from django.db import models
from unittest.util import _MAX_LENGTH

# Create your models here.

ROLECHOICE = (
    ('author','Author'),
    ('contributor','Contributor'),
    ('editor','Editor'),
    )

class Book(models.Model):
    title = models.CharField(max_length=200)
    volume = models.IntegerField(default=0)
    def __str__(self):
        return str(self.volume)+': '+self.title
    
class Person(models.Model):
    firstname = models.CharField(max_length=200)
    lastname  = models.CharField(max_length=200)
    def __str__(self):
        return self.lastname+', '+self.firstname
    
class BookPerson(models.Model):
    role = models.CharField(max_length=32, choices=ROLECHOICE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    def __str__(self):
        return self.person.lastname+', '+self.person.firstname+' was '+self.role+' of '+self.book.title
    
class Edition(models.Model):
    year = models.IntegerField(default=0)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    def __str__(self):
        return self.book.__str__()+' ('+str(self.year)+')'
    
class Instance(models.Model):
    condition = models.CharField(max_length=64)
    price = models.FloatField(default=0.00)
    edition = models.ForeignKey(Edition, on_delete=models.CASCADE)
    def __str__(self):
        return self.edition.__str__()+' ('+self.condition+', GBP '+str(self.price)+')'
    