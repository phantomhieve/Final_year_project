from django.db import models
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
    type = models.NullBooleanField(null = False, default = 0)

'''
    Stores the information of the users.
    - password stores hash of the actual password.
    - image stores hash of the image name on the disk.
    Relations
        - 'special' with special to indetify the type of user.
'''
class users(models.Model):
    u_name = models.CharField(max_length = 40, unique = True, null = False)
    password = models.CharField(max_length = 255, null = False)
    name = models.CharField(max_length = 64, null = False)
    dob = models.DateField(null = False)
    country = models.CharField(max_length = 64, null = False)
    email = models.EmailField(null = False)
    image = models.CharField(max_length = 255, null = True)
    contribution = models.IntegerField(default = 0)
    special = models.ForeignKey(special, on_delete=models.CASCADE, default = None)
