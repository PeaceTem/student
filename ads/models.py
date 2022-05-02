from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class PostAd(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    picture = models.ImageField(upload_to='images/',  blank=True, null=True)
    description = models.TextField(max_length=1000, blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    clicks = models.PositiveIntegerField(default=0)
    views = models.PositiveIntegerField(default=0)
    clickers = models.ManyToManyField(User, blank=True)
    detailpageviews = models.PositiveIntegerField(default=0)
    detailpageclicks = models.PositiveIntegerField(default=0)
    detailpagerelevance = models.FloatField(default=0)
    submitpageviews = models.PositiveIntegerField(default=0)
    submitpageclicks = models.PositiveIntegerField(default=0)
    submitpagerelevance = models.FloatField(default=0)

    bannerpageviews = models.PositiveIntegerField(default=0)
    bannerpageclicks = models.PositiveIntegerField(default=0)
    bannerpagerelevance = models.FloatField(default=0)

    correctionpageviews = models.PositiveIntegerField(default=0)
    correctionpageclicks = models.PositiveIntegerField(default=0)
    correctionpagerelevance = models.FloatField(default=0)


    def __str__(self):
        return f"{self.name}"