from django.contrib import admin

# Register your models here.

from .models import Book, Instance, Edition, Person, BookPerson

admin.site.register(Person)
admin.site.register(Book)
admin.site.register(Instance)
admin.site.register(Edition)
admin.site.register(BookPerson)