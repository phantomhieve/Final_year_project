from django.http import HttpResponse 
from django.shortcuts import render, get_object_or_404

from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response


from .models import Anime, Has_genre
from .serializers import AnimeSerializer

class AnimeView(APIView):
    def get(self, request):
        onePage=2
        page = int(request.query_params.get('page', 1)) - 1
        anime  = Anime.objects.filter(correct=True)[
            onePage*page:
            onePage*(page+1)
        ]
        anime_serializer = AnimeSerializer(anime, many= True)
        return Response(anime_serializer.data)
    def post(self, request):
        pass

class SingleAnimeView(APIView):
    pass
