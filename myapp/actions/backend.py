from .models import (
    user_views_anime,
    user_rates_anime,
)
from users.models import users
from anime.models import Anime

'''
Add view counts to given anime by given user

param: userId  (id field of the users)
param: animeId (id field of the Anime)

return: True  (added sucessfully)
return: False (not added sucessfully)
'''
def addView(userId, animeId):
    view = user_views_anime.objects.filter(user=userId, anime=animeId)
    if view:
        view[0].count+=1
        view[0].save()
        return True
    else:
        user  = users.objects.filter(id = userId)
        anime = Anime.objects.filter(id = animeId)
        if user and anime:
            view = user_views_anime(user=user[0], anime=anime[0])
            view.save()
            return True
    return False

'''
Adds the the rating to a anime by the user for a given anime.

param: userId  (id field of the users)
param: animeId (id field of the Anime)
param: rating  (rating provided by the user)

return: True  (added sucessfully)
return: False (not added sucessfully)
'''
def rateAnime(rating, userId, animeId):
    rate = user_rates_anime.objects.filter(user=userId, anime=animeId)
    if rate:
        rate[0].rating = rating
        rate[0].save()
        return True
    else:
        user  = users.objects.filter(id = userId)
        anime = Anime.objects.filter(id = animeId)
        if user and anime:
            rate = user_rates_anime(user=user[0], anime=anime[0], rating=rating)
            rate.save()
            return True
    return False
        

