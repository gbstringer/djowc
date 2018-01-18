from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import View 
from django.urls import reverse

from .models import Book, BookPerson, Person
from .forms import BookForm, AuthorForm

def index(request):
    book_list = Book.objects.order_by('title')
    person_list = BookPerson.objects.filter(role='author')
    context = {'book_list': book_list, 'person_list': person_list}
    return render(request, 'books/index.html', context)

class DetailView(View):
    def get(self, request, book_id):
        book = get_object_or_404(Book, pk=book_id)
        return render(request, 'books/detail.html' ,{'book': book})
    
class AuthorView(View):
    def get(self, request, person_id):
        author = get_object_or_404(Person, pk=person_id)
        return render(request, 'books/author.html', {'author':author})

class ListAuthorView(View):
    def get(self, request):
        author_list = Person.objects.order_by('lastname')
        return render(request, 'books/authors.html' ,{'author_list': author_list})

class AddBookView(View):
    def get(self, request):
        form=BookForm()
        return render(request,'books/add.html', {'form': form})
    def post(self, request):
        if request.method == 'POST':
            form=BookForm(request.POST)
            if form.is_valid(): 
                newbook = Book(title=request.POST['title'], volume=request.POST['volume'])
                newbook.save()
                return HttpResponseRedirect('/book/')
                #return reverse('books:index')
        else:
            form=BookForm()
        return render(request,'books/add.html', {'form': form}) 
    def get_success_url(self):
        return reverse('add')
    
def edit(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    new_title = book.title.get(pk=request.POST['title'])
    new_title.save()
    return render(request, 'books/edit.html', {'book': book})

class AddAuthorView(View):
    def get(self, request):
        form=AuthorForm()
        return render(request,'books/addauthor.html', {'form': form})
    def post(self, request):
        if request.method == 'POST':
            form=AuthorForm(request.POST)
            if form.is_valid(): 
                newauthor = Person(firstname=request.POST['firstname'], lastname=request.POST['lastname'])
                newauthor.save()
                return HttpResponseRedirect('books/authors/')
                #return reverse('books:index')
        else:
            form=AuthorForm()
        return render(request,'books/addauthor.html', {'form': form}) 
    def get_success_url(self):
        return reverse('addauthor')
    
class UpdateAuthorView(View):
    def get(self, request, person_id):
        author = get_object_or_404(Person, pk=person_id)
        new_firstname = author.firstname.get(pk=request.POST['firstname'])
        new_lastname = author.lastname.get(pk=request.POST['lastname'])
        new_firstname.save()
        new_lastname.save()
        return render(request, 'books/updateauthor.html', {'author': author})
   
def update(request,book_id):
    form = BookForm()
    return render(request, 'books/update.html', {'form':form})
    
'''    
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/')
    else: 
        form = BookForm()
    return render(request, 'books/update.html', {'form': form}) 
'''  
