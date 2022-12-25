from django.contrib.auth.models import User
from django.db import models

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class Kategori(models.Model):
    nama = models.CharField(max_length=20)

    def __str__(self):
        return self.nama

    class Meta:
        verbose_name_plural = "Kategori"

class Artikel(models.Model):
    nama = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    judul = models.CharField(max_length=100)
    deskripsi = RichTextUploadingField(blank=True, null=True,
                                            config_name='special',
                                            external_plugin_resources=[(
                                                'youtube',
                                                '/static/ckeditor_plugins/youtube/youtube/',
                                                'plugin.js',
                                                )],
    )
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to='artikel/thumbnail/', blank=True, null=True)

    def __str__(self):
        return "{} - {}".format(self.nama, self.judul)

    def ImgUrl(self):
        if self.thumbnail == '' or self.thumbnail == None:
            gambar = 'front/img/presentation-page/nasa.jpg'
        else:
            gambar = self.thumbnail
        return gambar

    class Meta:
        ordering =['-date']
        verbose_name_plural = "Artikel"

class Berita(models.Model):
    
    title = models.CharField(max_length=1000)
    link = models.CharField(max_length=1000)
    konten = models.TextField()
    date = models.CharField(max_length=1000)
    gambar = models.CharField(max_length=1000)

    def _str_(self) :
        return "{}" - "{}".format(self.nama, self.judul)