from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser
)
''' dont need this will remove at the time of making anime'''
class special(models.Model):
    username     = models.CharField(max_length = 255, primary_key = True)
    type         = models.NullBooleanField(null = False, default = None)

'''
    Stores the information of the users.
    - password stores hash of the actual password.
    - image stores hash of the image name on the disk.
    - type denotes type of user
        - None Common
        - 0 Special
        - 1 Admin
'''
class users(AbstractBaseUser):
    username      = models.CharField(max_length = 255, null = False, unique = True)
    password      = models.CharField(max_length = 255, null = False)
    name          = models.CharField(max_length = 255, null = False)
    dob           = models.DateField(max_length = 255, null = False)
    country       = models.CharField(max_length = 255, null = False)
    email         = models.EmailField(max_length = 225, unique = True)
    image         = models.CharField(max_length = 255, null = True)
    contribution  = models.IntegerField(default = 0)
    special       = models.NullBooleanField(default = None)

    USERNAME_FIELD = 'username'


