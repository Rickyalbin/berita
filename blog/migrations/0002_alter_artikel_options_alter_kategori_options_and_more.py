# Generated by Django 4.1.3 on 2022-11-30 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='artikel',
            options={'ordering': ['-date'], 'verbose_name_plural': 'Artikel'},
        ),
        migrations.AlterModelOptions(
            name='kategori',
            options={'verbose_name_plural': 'Kategori'},
        ),
        migrations.RenameField(
            model_name='artikel',
            old_name='kategory',
            new_name='kategori',
        ),
    ]
