from rest_framework import serializers

from collection.models import Collection
from collection.models import ComicCollection

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = (
            "id",
            "name",
            "slug",
            "get_absolute_url"
        )
        
class ComicCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComicCollection
        fields = (
            "id",
            "comic",
            "collection",
            "comic_detail",
            "collection_detail",
        )