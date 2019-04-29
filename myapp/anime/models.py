from django.db import models
from users.models import users


'''
    Stores the information of the animes.
    - image stores hash of the image name on the disk.
    Relations
        - 'users' with users to identify which user added it.
'''
class anime(models.Model):
    name  = models.CharField(max_length = 100, null = False)
    image = models.CharField(max_length = 255, null = False)
    r_date = models.DateField(null = False)
    info = models.TextField()
    user = models.ForeignKey(users, on_delete = models.SET_NULL, null = True)

'''
    Stores permanent anime.
    Relation
        - 'anime' with anime to identify permanent anime
'''
class permanent(models.Model):
    anime = models.ForeignKey(anime, on_delete = models.CASCADE)

'''
Stores temporary anime.
    Relation 
        - 'anime' with anime to identify temporary anime
'''
class temporary(models.Model):
    anime = models.ForeignKey(anime, on_delete = models.CASCADE)

'''
    Stores the possible genre of the animes.
'''
class genre(models.Model):
    type = models.CharField(max_length = 30, null = False)

'''
    Realtionship table (many - many)
        - primarykey = (anime, genre)
    - Denotes generes that a anime has.
'''
class has_genre(models.Model):
    anime = models.ForeignKey(anime, on_delete = models.CASCADE)
    genre = models.ForeignKey(genre, on_delete = models.CASCADE)
    class Meta:
        unique_together = (("anime", "genre"),)

'''
    Stores the seasons count (could use id too but mehh).
'''
class season(models.Model):
    num = models.IntegerField(null = False)

'''
    Realtionship table (many - many)
        - primarykey = (anime, season)
    - Denotes anime with seasons that has attribute count of episodes in a season.
'''
class has_seasons(models.Model):
    episodes = models.IntegerField(null = False)
    anime = models.ForeignKey(anime, on_delete = models.CASCADE)
    season = models.ForeignKey(season, on_delete = models.CASCADE)
    class Meta:
        unique_together = (("episodes", "anime","season"),)