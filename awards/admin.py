from django.contrib import admin
from .models import Categories, Profile, Project, Rating


# Register your models here.
admin.site.register(Categories)
admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(Rating)
