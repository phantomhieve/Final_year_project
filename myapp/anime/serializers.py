from rest_framework import serializers

from .models import Anime, Genre

class AnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Anime
        fields = ('id', 'name', 'image', 'info', 'release_date', 'average_rating', 'episodes')

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Genre
        fields = ('name',)

