# Generated by Django 4.2 on 2023-05-10 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comic', '0003_collection'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Collection',
        ),
    ]