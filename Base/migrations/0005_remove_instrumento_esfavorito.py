# Generated by Django 4.0 on 2022-05-16 22:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0004_remove_instrumento_tipoinstrumento_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instrumento',
            name='esFavorito',
        ),
    ]
