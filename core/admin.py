from django.contrib import admin
from .models import Profile, Streak, Follower
# Register your models here.

admin.site.register(Profile)
admin.site.register(Streak)
admin.site.register(Follower)

