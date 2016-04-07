from django import forms



class WrkForm(forms.Form):
    works=forms.CharField(max_length=100)
