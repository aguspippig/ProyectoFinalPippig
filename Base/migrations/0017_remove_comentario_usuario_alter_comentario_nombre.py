# Generated by Django 4.0 on 2022-05-24 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0016_delete_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentario',
            name='usuario',
        ),
        migrations.AlterField(
            model_name='comentario',
            name='nombre',
            field=models.CharField(max_length=40),
        ),
    ]
