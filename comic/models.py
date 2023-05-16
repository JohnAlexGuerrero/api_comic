from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files import File

from character.models import Character

class Comic(models.Model):
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField()
    publisher = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to="comics/", blank=True, null=True)
    thumbnail = models.ImageField(upload_to="comics/", blank=True, null=True)
    description = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name = ("Comic")
        verbose_name_plural = ("Comics")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'http://127.0.0.1:8000/api/v1/comics/{self.slug}'

    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()
                
                return 'http://127.0.0.1:8000' + self.thumbnail.url
            else:
                return ''
    
    def make_thumbnail(self, image, size=(400,300)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)
        
        thum_io = BytesIO()
        img.save(thum_io, 'JPEG', quality=85)
        
        thumbnail = File(thum_io, name=image.name)
        
        return thumbnail


class ComicCharacter(models.Model):
        comic = models.ForeignKey(Comic, verbose_name=("comics"), on_delete=models.CASCADE)
        character = models.ManyToManyField(Character, verbose_name=("characters"))
    
        class Meta:
            verbose_name = ("CharacterComic")
            verbose_name_plural = ("CharacterComics")
    
        def __str__(self):
            return self.comic.title
    
        def get_absolute_url(self):
            return f'http://127.0.0.1:8000/api/v1/characters/{self.comic.slug}/comics'
        