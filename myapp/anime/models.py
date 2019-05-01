from django.db import models
from users.models import users


'''
    Stores the possible genre of the animes.
'''
class Genre(models.Model):
    name = models.CharField(max_length = 30, null = False)

    def __str__(self):
        return self.name

'''
    Stores the information of the animes.
    - image stores hash of the image name on the disk.
    Relations
        - 'user' with users to identify which user added it.
        - 'genre' many to many relationship
    Episodes is a csv field where i'th index denotes episodes 
    in i+1 Season
'''
class Anime(models.Model):
    name           = models.CharField(max_length = 255, null = False)
    image          = models.ImageField(upload_to = 'anime_image', blank = True)
    release_date   = models.DateField(null = False)
    info           = models.TextField()
    correct        = models.BooleanField(default=False)
    average_rating = models.IntegerField(default=0)
    episodes       = models.CharField(max_length = 255, null=True, default=None)
    user           = models.ForeignKey(users, on_delete = models.SET_NULL, null = True)
    # many to many relationship : anime  <-> Genre
    genre          = models.ManyToManyField(Genre, blank=True)
    
    def __str__(self):
        status = '(Permanent)' if self.correct else '(Temporary)'
        return F"{self.name} {status}"



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
