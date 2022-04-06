from django.db import models

# Create your models here.

class PostAd(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    picture = models.ImageField(upload_to='images/',  blank=True, null=True)
    description = models.TextField(max_length=1000, blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    clicks = models.PositiveIntegerField(default=0)



    