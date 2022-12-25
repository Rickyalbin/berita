from django.contrib import admin
from.models import *
# Register your models here.

class ArtikelAdmin(admin.ModelAdmin):
    list_display = ('nama', 'judul', 'deskripsi', 'kategori', 'date')

admin.site.register(Kategori)
admin.site.register(Artikel, ArtikelAdmin)

class BeritaAdmin(admin.ModelAdmin):
    list_display = ('title','link','konten','date','gambar')

admin.site.register(Berita,BeritaAdmin)