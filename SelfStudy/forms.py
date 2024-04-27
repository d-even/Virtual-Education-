from turtle import textinput
from django import forms

class Cookie(forms.Form):
    Name=forms.CharField(label="Name",required=False,widget=forms.TextInput(attrs={'class':"form-control"}))
    Email=forms.EmailField(label="Email",widget=forms.TextInput(attrs={'class':"form-control"}))
    Phone=forms.CharField(label="Phone",required=False,widget=forms.TextInput(attrs={'class':"form-control"}))