from django.http import Http404,HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import View 
from django.urls import reverse
# Create your views here.

from .models import Book
from .forms import BookForm

def index(request):
    latest_book_list = Book.objects.order_by('title')[:5]
    context = {'latest_book_list': latest_book_list}
    return render(request, 'books/index.html', context)

def detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'books/detail.html', {'book': book})

'''
def add(request):
    if request.method == 'POST':
        
        form = BookForm(request.POST)
        if form.is_valid():
            
            newbook = Book(title=form.title)
            newbook.save()
            return HttpResponseRedirect('/book/')
        
            
    else:
        form = BookForm()
        
    return render(request,'books/add.html', {'form': form})
'''

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
                return HttpResponse('form valid: '+newbook.title)
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
'''    

def update(request,book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/book/')
    else:
        form = BookForm()
    return render(request, 'update.html', {'form': form})
    
'''    
    
   
   
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
    

'''
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
'''    
