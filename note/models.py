from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# add images
class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100, blank=True, null=True)
    topic = models.CharField(max_length=200, blank=True, null=True)
    note_detail = models.TextField(max_length=100000)
    date_updated = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date_created', '-date_updated']


    def __str__(self):
        return f"{self.topic}"