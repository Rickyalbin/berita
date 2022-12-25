from django import forms
from django.contrib.auth.models import User
from .models import Biodata

class UserForms(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'first_name', 'email')
        widgets ={
            "first_name" : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'type':'text',
                    'placeholder':"Judul Artikel",
                    'required':True
                }),
            "first_name" : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'type':'text',
                    'placeholder':"Judul Artikel",
                    'required':True
                }),
            "email" : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'type':'text',
                    'placeholder':"Judul Artikel",
                    'required':True
                }),
        }
class Biodataforms(forms.ModelForm):
    class Meta:
        model = Biodata
        fields = ('alamat', 'telp')
        widgets ={
            "alamat" : forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'type':'text',
                    'placeholder':"Judul Artikel",
                    'required':True
                }),
            "telp" : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'type':'text',
                    'placeholder':"Judul Artikel",
                    'required':True
                }),
        }