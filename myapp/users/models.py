from django.db import models
from datetime import date
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

''' dont need this will remove at the time of making anime'''
class special(models.Model):
    username     = models.CharField(max_length = 255, primary_key = True)
    type         = models.NullBooleanField(null = False, default = None)


class usersManager(BaseUserManager):
    
    def create_user(self, email, username, country, name, password):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('User must have email')

        email = self.normalize_email(email)
        user = self.model(
            email=email, 
            username=username,
            dob=date(1996, 3, 28),
            country= country,
            name= name  
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email, username, country, name, password):
        """
        Creates and saves a superuser with the given email, username
        and password.
        """
        user = self.create_user(email, username, country, name, password)
        user.is_admin     = True
        user.is_superuser = True
        user.save(using=self._db) 
        return user


'''
    Stores the information of the users.
    - password stores hash of the actual password.
    - image stores hash of the image name on the disk.
    - tpyes of user
        admin     = is_admin = True
        moderator = is_admin = False, is_mod = True
        General   = is_admin = False, is_mod = False
'''
class users(AbstractBaseUser, PermissionsMixin):
    username      = models.CharField(max_length = 255, unique = True)
    name          = models.CharField(max_length = 255, null = True)
    dob           = models.DateField(max_length = 255, null = True)
    country       = models.CharField(max_length = 255, null = True)
    email         = models.EmailField(max_length = 225, unique = True, null = True)
    image         = models.ImageField(upload_to = 'profile_image/', blank = True)
    contribution  = models.IntegerField(default = 0)
    is_mod        = models.NullBooleanField(default = False)

    # default fields
    is_admin      = models.NullBooleanField(default = False)
    is_active     = models.BooleanField(default=True)
    is_staff      = models.BooleanField(default=True)
    is_superuser  = models.BooleanField(default=False)

    objects = usersManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'country', 'name']
    
    def __str__(self):
        return self.username

