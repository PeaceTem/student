from django.db import models
from django.contrib.auth.models import User
# from ckeditor.fields import RichTextField
# Create your models here.

class Diary(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100, blank=True, null=True, default='This is the diary title.')
   # photo = models.ImageField(upload_to='core\\static\\image')
   # add richtextfield
    post = models.TextField()
    # post = RichTextField()
    author = models.CharField(max_length=30)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    isAnAd = models.BooleanField(default=False)


    class Meta:
        ordering = ['-date_updated', '-date_created']
        verbose_name_plural = 'Diaries'