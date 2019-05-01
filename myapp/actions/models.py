from django.db import models
from anime.models import Anime, Temporary, Permanent
from users.models import users, special

'''
    Realtionship table (many - many)
        - primarykey = (user, anime)
    - Denotes anime viewed by user.
'''

class user_views_anime(models.Model):
    count = models.IntegerField(default=1)
    user  = models.ForeignKey(users, on_delete = models.CASCADE)
    anime = models.ForeignKey(Anime, on_delete = models.CASCADE)
    class Meta:
        unique_together = ((('user', 'anime'),))
    
    def __str__(self):
        return (
            F"({self.user.username} {self.anime.name})-> {self.count}"
        )

'''
    Realtionship table (many - many)
        - primarykey = (user, anime)
    - Denotes rating of a anime by a user.
'''
class user_rates_anime(models.Model):
    rating = models.IntegerField(null = False)
    user = models.ForeignKey(users, on_delete = models.CASCADE)
    anime = models.ForeignKey(Anime, on_delete = models.CASCADE)
    class Meta:
        unique_together = ((('user', 'anime'),))

'''
    Realtionship table (Ternary)
        - primarykey = (user, temporary, permanent)
    - Denotes the changes made on permanent stored in temporay by user.
'''
class edits(models.Model):
    user = models.ForeignKey(users, on_delete = models.CASCADE)
    temporary = models.ForeignKey(Temporary, on_delete = models.SET_NULL, null = True)
    permanent = models.ForeignKey(Permanent, on_delete = models.CASCADE)
    class Meta:
        unique_together = ((('user', 'temporary','permanent'),))


'''
    Relationship table (Ternary)
        - primarykey = (special, public, anime)
    - Denotes the anime verified by special edited by public stored in permanent.
'''
class final(models.Model):
    special = models.ForeignKey(special, on_delete = models.SET_NULL, null = True)
    public = models.ForeignKey(users, on_delete = models.SET_NULL, null = True)
    anime = models.ForeignKey(Permanent, on_delete = models.CASCADE)
    class Meta:
        unique_together = ((('special', 'public','anime'),))
