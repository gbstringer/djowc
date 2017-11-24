from django.http import Http404,HttpResponse
from django.shortcuts import get_object_or_404, render
# Create your views here.

from .models import Book

def index(request):
    latest_book_list = Book.objects.order_by('book_title')[:5]
    context = {'latest_book_list': latest_book_list}
    return render(request, 'books/index.html', context)


def detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'books/detail.html', {'book': book})

'''
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
'''    
