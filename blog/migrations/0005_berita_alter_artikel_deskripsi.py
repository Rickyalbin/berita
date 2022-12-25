# Generated by Django 4.1.3 on 2022-12-24 08:11

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_artikel_thumbnail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Berita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=100)),
                ('konten', models.TextField()),
                ('date', models.CharField(max_length=100)),
                ('gambar', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='artikel',
            name='deskripsi',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
