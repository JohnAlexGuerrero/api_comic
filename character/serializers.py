from rest_framework import serializers

from character.models import Character

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = (
            "id",
            "name",
            "gender",
            "species",
            "get_avatar",
            "get_absolute_url"
        )