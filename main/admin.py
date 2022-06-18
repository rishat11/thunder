from django.contrib import admin

from main.models import UserPhoto, UserProfile

admin.site.register(UserProfile)
admin.site.register(UserPhoto)
