
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile, Streak, Follower
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session

from importlib import import_module
from django.conf import settings
SessionStore = import_module(settings.SESSION_ENGINE).SessionStore

"""
Whenever a user is created, loop through the sessionstore
"""


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        Follower.objects.create(user=instance)

# post_save.connect(create_profile, sender=User)

# @receiver(post_save, sender=User)
# def update_profile(sender, instance, created, *args, **kwargs):
#     if created == False:
#         instance.profile.save()
        
# post_save.connect(update_profile, sender=User)


@receiver(post_save, sender=Profile)
def create_streak(sender, instance, created, *args, **kwargs):
    if created:
        # add the referral code here


        Streak.objects.create(profile=instance)


# This should be called update_streak





