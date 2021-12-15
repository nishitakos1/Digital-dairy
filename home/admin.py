from django.contrib import admin
from .models import BlogModels, Profile

# Register your models here.

admin.site.register(BlogModels)
admin.site.register(Profile)

