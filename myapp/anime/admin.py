from django.contrib import admin

# Register your models here.
from .models import anime, permanent, temporary, genre, has_genre, season, has_seasons

admin.site.register(anime)
admin.site.register(permanent)
admin.site.register(temporary)
admin.site.register(genre)
admin.site.register(has_genre)
admin.site.register(season)
admin.site.register(has_seasons)
