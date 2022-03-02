
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserPageCounter



@receiver(post_save, sender=User)
def create_analysis(sender, instance, created, *args, **kwargs):
    if created:
        UserPageCounter.objects.create(user=instance)



