# Generated by Django 4.2 on 2023-05-10 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comiccollection',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='comiccollection',
            name='title',
        ),
    ]
