from django.db import models
from anime.models import anime, temporary, permanent
from users.models import users, special
'''
    Realtionship table (many - many)
        - primarykey = (user, anime)
    - Denotes anime viewed by user.
'''
class views(models.Model):
    user = models.ForeignKey(users, on_delete = models.CASCADE)
    anime = models.ForeignKey(anime, on_delete = models.CASCADE)
    class Meta:
        unique_together = ((('user', 'anime'),))

'''
    Realtionship table (many - many)
        - primarykey = (user, anime)
    - Denotes rating of a anime by a user.
'''
class rates(models.Model):
    rating = models.IntegerField(null = False)
    user = models.ForeignKey(users, on_delete = models.CASCADE)
    anime = models.ForeignKey(anime, on_delete = models.CASCADE)
    class Meta:
        unique_together = ((('user', 'anime'),))

'''
    Realtionship table (Ternary)
        - primarykey = (user, temporary, permanent)
    - Denotes the changes made on permanent stored in temporay by user.
'''
class edits(models.Model):
    user = models.ForeignKey(users, on_delete = models.CASCADE)
    temporary = models.ForeignKey(temporary, on_delete = models.SET_NULL, null = True)
    permanent = models.ForeignKey(permanent, on_delete = models.CASCADE)
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
    anime = models.ForeignKey(permanent, on_delete = models.CASCADE)
    class Meta:
        unique_together = ((('special', 'public','anime'),))

