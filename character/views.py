from django.shortcuts import render
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response

from character.models import Character

from character.serializers import CharacterSerializer

class CharactersView(APIView):
    def get(self, request, format=None):
        query = Character.objects.all()
        serializer = CharacterSerializer(query, many=True)
        
        return Response(serializer.data)

class CharacterDetailView(APIView):
    def get_object(self, character_slug):
        try:
            return Character.objects.get(slug=character_slug)
        except Character.DoesNotExist:
            raise Http404
        
    def get(self, request, **kwargs):
        character = self.get_object(self.kwargs["character_slug"])
        serializer = CharacterSerializer(character)
        
        return Response(serializer.data)