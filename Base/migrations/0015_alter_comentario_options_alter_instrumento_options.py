# Generated by Django 4.0 on 2022-05-24 00:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0014_comentario_nombre'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comentario',
            options={'ordering': ['-fechaComentario']},
        ),
        migrations.AlterModelOptions(
            name='instrumento',
            options={'ordering': ['-fechaPublicacion']},
        ),
    ]
