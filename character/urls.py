from django.urls import path

from character.views import CharactersView
from character.views import CharacterDetailView

urlpatterns = [
    path('', CharactersView.as_view(), name='characters'),
    path('<slug:character_slug>/', CharacterDetailView.as_view(), name='character_detail'),
]
