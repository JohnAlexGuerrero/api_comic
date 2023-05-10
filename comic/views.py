from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from comic.models import Comic

from comic.serializers import ComicSerializer

class ComicsView(APIView):
    def get(self,request, format=None):
        query = Comic.objects.all().order_by('created_at')
        serializer = ComicSerializer(query, many=True)
        
        return Response(serializer.data)
