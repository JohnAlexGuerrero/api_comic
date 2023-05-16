from django.contrib import admin

from comic.models import Comic
from comic.models import ComicCharacter

admin.site.register(Comic)
admin.site.register(ComicCharacter)