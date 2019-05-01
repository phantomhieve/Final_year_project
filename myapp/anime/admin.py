from django.contrib import admin

# Register your models here.
from .models import Anime, Permanent, Temporary, Genre 

admin.site.register(Anime)
admin.site.register(Permanent)
admin.site.register(Temporary)
admin.site.register(Genre)