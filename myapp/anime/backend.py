from .models import Anime, Genre
from math import ceil
onePage = 9

def getAnimePageData(page, status):
    anime  = Anime.objects.filter(correct=status)[
            onePage*page:
            onePage*(page+1)
        ]
    return anime

def getAnimeData(animeId):
    anime = Anime.objects.filter(id = animeId)
    if len(anime)==0: return False
    return anime

def getPermanentAnimePageCount(status):
    anime =  Anime.objects.filter(correct=status)
    return int(ceil(len(anime)/onePage))