from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)



    @property
    def last_update(self):
        days_length = date.today() - self.updated.date()
        days_length_shrink = str(days_length).split(',', 1)[0]
        return days_length_shrink


    @property
    def when_joined(self):
        days_length = date.today() - self.created.date()
        days_length_shrink = str(days_length).split(',', 1)[0]
        return days_length_shrink


    def __str__(self):
        return self.title
    

    class Meta:
        ordering = ['complete', '-created']