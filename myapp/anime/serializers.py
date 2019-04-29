from rest_framework import serializers

from .models import Anime, Has_genre

class AnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Anime
        fields = ('id', 'name', 'image', 'info', 'release_date', 'average_rating', 'episodes')

