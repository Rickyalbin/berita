from re import template
import re
from django.http import request
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test 

from django.contrib.auth.models import User

from .models import Artikel, Kategori, Berita
from .forms import ArtikelForms
import requests
# Create your views here.

@login_required
def dashboard(request):
    if request.user.groups.filter(name='Operator').exists():
        request.session['is_operator'] = 'operator'

    template_name = "back/dashboard.html"
    context = {
        'title': 'Dashboard',
    }
    return render(request, template_name, context)

@login_required
def berita(request):
    template_name = "back/tabel_berita.html"
    berita = Berita.objects.all()
    context = {
        'title': 'Tabel Berita',
        'berita':berita,
    }
    return render(request, template_name, context)

@login_required
def artikel(request):
    template_name = "back/tabel_artikel.html"
    artikel = Artikel.objects.filter(nama = request.user)
    context = {
        'title': 'List Berita Indonesia',
        'artikel':artikel,
    }
    return render(request, template_name, context)

@login_required
def tambah_artikel(request):
    template_name = "back/tambah_artikel.html"
    kategori = Kategori.objects.all()
   
    if request.method == "POST":
        forms_artikel = ArtikelForms(request.POST, request.FILES)
        if forms_artikel.is_valid():
            art = forms_artikel.save(commit=False)
            art.nama = request.user
            art.save()
            return redirect(artikel)
    
    else:
        forms_artikel = ArtikelForms()
        pass
    context = {
        'title': 'Tambah Berita',
        'kategori':kategori,
        'forms_artikel':forms_artikel
    }
    return render(request, template_name, context)

@login_required
def lihat_artikel(request, id):
    template_name = "back/lihat_artikel.html"
    artikel = Artikel.objects.get(id=id)
    context = {
        'title': 'Views Berita',
        'artikel':artikel,
    }
    return render(request, template_name, context)

@login_required
def edit_artikel(request, id):
    template_name = "back/tambah_artikel.html"
    a = Artikel.objects.get(id=id)
    if request .method == "POST":
        forms_artikel = ArtikelForms(request.POST, request.FILES, instance=a)
        if forms_artikel.is_valid():
            art = forms_artikel.save(commit=False)
            art.nama = request.user
            art.save()
            return redirect(artikel)        
    else:
        forms_artikel = ArtikelForms(instance=a)

    context = {
        'title': 'Edit Berita',
        'artikel':a,
        'forms_artikel':forms_artikel
    }    
    return render(request, template_name, context)

@login_required
def delete_artikel(request, id):
    Artikel.objects.get(id=id).delete()
    return redirect(artikel)

def sinkron_berita(request):
	url = "https://berita-indo-api.vercel.app/v1/cnn-news"
	data = requests.get(url).json()
	for d in data['data']:
		cek_berita = Berita.objects.filter(title=d['title'])
		if cek_berita:
			print('data sudah ada')
			c = cek_berita.first()
			c.title=d['title']
			c.save()
		else: 
      		#jika belum ada maka tulis baru kedatabase
			b = Berita.objects.create(
				title = d['title'],
				link = d['link'],
				konten = d['contentSnippet'],
				date = d['isoDate'],
				gambar = d['image'],
			
			)
	return redirect(berita)
    
