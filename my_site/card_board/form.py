from django import forms

class Rform(forms.Form):
    name = forms.CharField(label="name",max_length=100)