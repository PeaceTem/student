
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile, Streak
from django.contrib.auth.models import User



@receiver(post_save, sender=User)
def create_profile(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# post_save.connect(create_profile, sender=User)

# @receiver(post_save, sender=User)
# def update_profile(sender, instance, created, *args, **kwargs):
#     if created == False:
#         instance.profile.save()
        
# post_save.connect(update_profile, sender=User)


@receiver(post_save, sender=Profile)
def create_streak(sender, instance, created, *args, **kwargs):
    if created:
        Streak.objects.create(profile=instance)




@receiver(post_save, sender=Profile)
def create_streak(sender, instance, created, *args, **kwargs):
    if created == False:
        instance.streak.save()














