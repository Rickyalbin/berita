from django import forms
from .models import Artikel
from django.forms import widgets
from .models import Artikel

class ArtikelForms(forms.ModelForm):
    class Meta:
        model = Artikel
        fields = ('judul', 'deskripsi', 'kategori', 'thumbnail')
        widgets = {
            "judul" : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'type':'text',
                    'placeholder':"Judul Berita",
                    'required':True
                }),
                
            "deskripsi" : forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'cols':'30',
                    'rows':'10',
                    'required':True
                }),
            "kategori" : forms.Select(
                attrs={
                    'class': 'form-control',
                    'type':'text',
                    'required':True,
                }),
        
        }

