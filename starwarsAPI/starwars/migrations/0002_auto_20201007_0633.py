# Generated by Django 3.1.2 on 2020-10-07 06:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('starwars', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='characters',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='producers',
        ),
    ]