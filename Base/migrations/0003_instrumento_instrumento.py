# Generated by Django 4.0 on 2022-05-16 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0002_remove_bajo_instrumento_remove_bateria_instrumento_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='instrumento',
            name='instrumento',
            field=models.CharField(choices=[('guitarra', 'GUITARRA'), ('bajo', 'BAJO'), ('pedal', 'PEDAL'), ('bateria', 'BATERIA'), ('teclado', 'TECLADO'), ('amplificador', 'AMPLIFICADOR')], default='guitarra', max_length=15),
        ),
    ]
