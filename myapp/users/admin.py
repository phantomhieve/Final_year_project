from django.contrib import admin

from .forms import UserAdmin, Group 
from .models import users, special

admin.site.register(users, UserAdmin)
admin.site.register(special)
admin.site.unregister(Group)