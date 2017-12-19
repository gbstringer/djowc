'''
Created on 7 Dec 2017

@author: gbstring
'''

from django import forms

class BookForm(forms.Form):
    title = forms.CharField(label='Title',
                            max_length=63,
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    volume=forms.IntegerField(max_value=999, min_value=1, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    
    
