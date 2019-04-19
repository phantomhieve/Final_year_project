from django.contrib import admin

# Register your models here.
from .models import views, rates, edits, final

admin.site.register(views)
admin.site.register(rates)
admin.site.register(edits)
admin.site.register(final)