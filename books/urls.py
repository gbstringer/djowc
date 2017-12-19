'''
Created on 23 Nov 2017

@author: gbstring
'''
from django.conf.urls import url

from . import views
from books.views import AddBookView


app_name = 'books'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<book_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
#    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
#    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

#    url(r'^add/$', views.add, name='add'),
    url(r'^add/$',AddBookView.as_view(), name='add'),
    
    url(r'^(?P<book_id>[0-9]+)/edit/$', views.edit, name='edit'),
    url(r'^(?P<book_id>[0-9]+)/update/$', views.update, name='update'),

    ]