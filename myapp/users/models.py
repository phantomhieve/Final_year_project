from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser
)
'''
    Special user stores weather a user is
        - Moderator
        - Admin
        - Public
    In case of public we store NULL in foreign key column of users.
    In case of moderator we store '0' in type which is default.
    In case of Admin we store '1'.
'''
class special(models.Model):
    username     = models.CharField(max_length = 255, primary_key = True)
    type         = models.NullBooleanField(null = False, default = None)

'''
    Stores the information of the users.
    - password stores hash of the actual password.
    - image stores hash of the image name on the disk.
    Relations
        - 'special' with special to indetify the type of user.
'''
class users(AbstractBaseUser):
    username      = models.CharField(max_length = 255, null = False, unique = True)
    name          = models.CharField(max_length = 255, null = False)
    dob           = models.DateField(max_length = 255, null = False)
    country       = models.CharField(max_length = 255, null = False)
    email         = models.EmailField(max_length = 225, unique = True)
    image         = models.CharField(max_length = 255, null = True)
    contribution  = models.IntegerField(default = 0)
    special       = models.ForeignKey(special, on_delete=models.CASCADE,)

    USERNAME_FIELD = 'username'


