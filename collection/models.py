from django.db import models

from comic.models import Comic

class Collection(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField()
    
    class Meta:
        verbose_name = ("Collection")
        verbose_name_plural = ("Collections")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'http://127.0.0.1:8000/api/v1/collections/{self.slug}'
    
class ComicCollection(models.Model):
    comic = models.ForeignKey(Comic, verbose_name=("comics"), on_delete=models.CASCADE)
    collection = models.ForeignKey(Collection, verbose_name=("collections"), on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = ("ComicCollection")
        verbose_name_plural = ("ComicCollections")

    def __str__(self):
        return f'{self.collection.name}'

    def get_absolute_url(self):
        return f'{self.collection.slug}'

    def comic_detail(self):
        collections = {
            "id": self.comic.id,
            "title": self.comic.title,
            #"thumbnail": self.comic.get_thumbnail(),
            "url": self.collection.get_absolute_url()
        }
        
        return collections

    def collection_detail(self):
        comic = {
            "id": self.collection.id,
            "title": self.collection.name,
            "thumbnail": self.comic.get_thumbnail(),
            "url": self.collection.get_absolute_url()
        }
        
        return comic