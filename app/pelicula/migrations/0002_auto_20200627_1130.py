# Generated by Django 3.0.7 on 2020-06-27 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pelicula', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='nombre_sala',
            new_name='nombres',
        ),
    ]
