from django.contrib import admin

# Register your models here.
from .models import users, special

admin.site.register(users)
admin.site.register(special)