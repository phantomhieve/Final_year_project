from django.contrib import admin

# Register your models here.
from .models import(
        user_rates_anime,
        user_views_anime,
        edits,
        final,
) 

admin.site.register(user_views_anime)
admin.site.register(user_rates_anime)
admin.site.register(edits)
admin.site.register(final)