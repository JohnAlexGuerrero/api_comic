from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404

from collection.serializers import CollectionSerializer
from collection.serializers import ComicCollectionSerializer

from collection.models import Collection
from collection.models import ComicCollection


class CollectionsView(APIView):
    def get(self, request, format=None):    
        query = Collection.objects.all()
        serializer = CollectionSerializer(query, many=True)
        
        return Response(serializer.data)


class ComicCollectionView(APIView):
    def get_object(self, collection_slug):
        try:
            return ComicCollection.objects.filter(collection__slug=collection_slug)
        except ComicCollection.DoesNotExist:
            raise Http404
    
    def get(self, request, collection_slug, format=None):
        comics = self.get_object(collection_slug)
        serializer = ComicCollectionSerializer(comics, many=True)

        return Response(serializer.data)
    