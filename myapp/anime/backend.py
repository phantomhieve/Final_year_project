from .models import Anime, Genre
from math import ceil
onePage = 9
def getAnimePageData(page):
    anime  = Anime.objects.filter(correct=True)[
            onePage*page:
            onePage*(page+1)
        ]
    return anime

def getAnimeData(animeId):
    anime = Anime.objects.filter(id = animeId)
    if len(anime)==0: return False
    return anime

def getPermanentAnimePageCount():
    anime =  Anime.objects.filter(correct=True)
    return int(ceil(len(anime)/onePage))