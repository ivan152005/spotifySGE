# Generated by Django 5.1.4 on 2025-01-23 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bdSpotify', '0010_alter_cancion_genero'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TablaTemporalGenero',
        ),
    ]
