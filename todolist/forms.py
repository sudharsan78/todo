from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    works=forms.CharField(max_length=100)
    
	
