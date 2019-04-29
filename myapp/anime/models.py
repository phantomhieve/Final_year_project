from django.db import models
from users.models import users


'''
    Stores the information of the animes.
    - image stores hash of the image name on the disk.
    Relations
        - 'by_users' with users to identify which user added it.
'''
class Anime(models.Model):
    name           = models.CharField(max_length = 100, null = False)
    image          = models.ImageField(upload_to = 'anime_image', blank = True)
    release_date   = models.DateField(null = False)
    info           = models.TextField()
    correct        = models.BooleanField(default=False)
    episodes       = models.IntegerField(default=0)
    average_rating = models.IntegerField(default=0)
    user           = models.ForeignKey(users, on_delete = models.SET_NULL, null = True)
    
    def __str__(self):
        return self.name + ' ' + str(self.correct)
'''
    Stores the possible genre of the animes.
'''
class Genre(models.Model):
    type = models.CharField(max_length = 30, null = False)
    
    def __str__(self):
        return self.type

'''
    Realtionship table (many - many)
        - primarykey = (anime, genre)
    - Denotes generes that a anime has.
'''
class Has_genre(models.Model):
    anime = models.ForeignKey(Anime, on_delete = models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete = models.CASCADE)
    class Meta:
        unique_together = (("anime", "genre"),)
    
    def __str__(self):
        return str(self.genre)+' '+ str(self.anime)

#  WONT NEED THIS (For further improvement)
'''
    Stores permanent anime.
    Relation
        - 'anime' with anime to identify permanent anime
'''
class Permanent(models.Model):
    anime = models.ForeignKey(Anime, on_delete = models.CASCADE)

'''
Stores temporary anime.
    Relation 
        - 'anime' with anime to identify temporary anime
'''
class Temporary(models.Model):
    anime = models.ForeignKey(Anime, on_delete = models.CASCADE)

'''
    Stores the seasons count (could use id too but mehh).
'''
class Season(models.Model):
    num = models.IntegerField(null = False)

'''
    Realtionship table (many - many)
        - primarykey = (anime, season)
    - Denotes anime with seasons that has attribute count of episodes in a season.
'''
class Has_seasons(models.Model):
    episodes  = models.IntegerField(null = False)
    anime     = models.ForeignKey(Anime, on_delete = models.CASCADE)
    season    = models.ForeignKey(Season, on_delete = models.CASCADE)
    class Meta:
        unique_together = (("episodes", "anime","season"),)
