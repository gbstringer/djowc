'''
Created on 23 Nov 2017

@author: gbstring
'''
from django.conf.urls import url

from . import views
from books.views import AddBookView, DetailView, AuthorView, ListAuthorView, UpdateAuthorView, AddAuthorView


app_name = 'books'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    # url(r'^(?P<book_id>[0-9]+)/$', views.detail, name='detail'),
    
    url(r'^(?P<book_id>[0-9]+)/detail/$', DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
#    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
#    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

    url(r'^authors/$',ListAuthorView.as_view(), name='authors'),
    url(r'^author/(?P<person_id>[0-9]+)/$', AuthorView.as_view(), name='author'),
    url(r'^author/(?P<person_id>[0-9]+)/update/$',UpdateAuthorView.as_view(), name='updateauthor'),
    url(r'^author/add/$', AddAuthorView.as_view(), name='addauthor'),


#    url(r'^add/$', views.add, name='add'),
    url(r'^add/$',AddBookView.as_view(), name='add'),
    url(r'^(?P<book_id>[0-9]+)/edit/$', views.edit, name='edit'),
    url(r'^(?P<book_id>[0-9]+)/update/$', views.update, name='update'),

    ]