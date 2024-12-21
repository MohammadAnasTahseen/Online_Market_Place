from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from items.models import *

input_classes = 'w-full py-4 px-5 rounded-xl border'
class NewItemForm(forms.ModelForm):
    class Meta:
        model=Item
        fields=['category','name','description','price','image']
        
        widgets={
            'category':forms.Select(attrs={
                'class': input_classes
                
                
            }),
            
            'name':forms.TextInput(attrs={
                'class': input_classes
                
                
            }),
             'description':forms.Textarea(attrs={
                'class': input_classes
                
                
            }),
            'price':forms.TextInput(attrs={
            'class': input_classes
                
                
            }),
                'image':forms.FileInput(attrs={
                 'class': input_classes
                
                
            }),
            
            
            
        }
        
        
class EditItemForm(forms.ModelForm):
    class Meta:
        model=Item
        fields=['name','description','price','image','is_sold']
        
        widgets={
            'name':forms.TextInput(attrs={
                'class': input_classes
                
                
            }),
             'description':forms.Textarea(attrs={
                'class': input_classes
                
                
            }),
            'price':forms.TextInput(attrs={
            'class': input_classes
                
                
            }),
                'image':forms.FileInput(attrs={
                 'class': input_classes
                
                
            }),
            
            
            
        }