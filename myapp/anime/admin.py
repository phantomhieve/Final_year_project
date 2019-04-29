from django.contrib import admin

# Register your models here.
from .models import Anime, Permanent, Temporary, Genre, Has_genre, Season, Has_seasons

admin.site.register(Anime)
admin.site.register(Permanent)
admin.site.register(Temporary)
admin.site.register(Genre)
admin.site.register(Has_genre)
admin.site.register(Season)
admin.site.register(Has_seasons)
