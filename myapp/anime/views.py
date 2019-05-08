from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout, get_user
from django.shortcuts import render, redirect
from django.http import HttpResponse

from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.permissions import IsAuthenticated



from .models import Anime, Genre
from .serializers import AnimeSerializer, GenreSerializer
from actions.backend import addView

class AnimeView(APIView):
    '''
    API gives back JSON data with anime information of count
    define in 'onePage'.

    requirement: GET param: page (next onePage anime data)

    return JSON format (each field):
    {
        id, name, image , info, release_date, average_rating, 
        episodes (csv field i'th index denotes episodes in i+1 Season)
    }
    '''
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
    '''
    API gives back JSON data with anime information and adds 
    view for the user to the anime.

    requirement: GET param: userId  (denotes the id of the user)
                            animeId (denotes the id of the anime)
    
    return JSON format(field):
    {
        'anime':[
            id, name, image , info, release_date, average_rating, 
                episodes (csv field i'th index denotes episodes in i+1 Season)
        ]
        'genre':[
            name: 'genre'
            name: 'genre',
            ....
            ....
        ]
    }
    '''
    def get(self, request):
        animeId = int(request.query_params.get('animeId', 1))
        userId  = request.query_params.get('userId', None)
        if userId: addView(int(userId), animeId)
        anime     = Anime.objects.filter(id = animeId)
        genre     = anime[0].genre.all()
        anime_serializer = AnimeSerializer(anime, many=True)
        genre_serializer = GenreSerializer(genre, many=True)
        return Response({
            'anime': anime_serializer.data,
            'genre': genre_serializer.data,
        })
            
    def post(self, request):
        pass

@login_required()
def main_view(request):
    args = {
        'user': request.user
    }
    return render(request, 'anime/main.html', args)