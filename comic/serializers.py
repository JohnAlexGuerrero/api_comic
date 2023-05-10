from rest_framework import serializers

from comic.models import Comic

class ComicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comic
        fields = (
            "id",
            "title",
            "description",
            "get_absolute_url",
            "get_thumbnail",
            "publisher"
        )