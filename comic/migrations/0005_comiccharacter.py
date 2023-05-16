# Generated by Django 4.2 on 2023-05-16 20:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('character', '0002_character_is_hero_character_species'),
        ('comic', '0004_delete_collection'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComicCharacter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('character', models.ManyToManyField(to='character.character', verbose_name='characters')),
                ('comic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comic.comic', verbose_name='comics')),
            ],
            options={
                'verbose_name': 'CharacterComic',
                'verbose_name_plural': 'CharacterComics',
            },
        ),
    ]