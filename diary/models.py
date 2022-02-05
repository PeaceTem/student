from django.db import models
from django.contrib.auth.models import User
from datetime import date
# from ckeditor.fields import RichTextField
# Create your models here.


class Diary(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100, blank=True, null=True, default='This is the diary title.')
    photo = models.ImageField(null=True, blank=True)
    post = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


    @property
    def last_update(self):
        days_length = date.today() - self.date_updated.date()
        days_length_shrink = str(days_length).split(',', 1)[0]
        return days_length_shrink


    @property
    def when_created(self):
        days_length = date.today() - self.date_joined.date()
        days_length_shrink = str(days_length).split(',', 1)[0]
        return days_length_shrink


    def __str__(self):
        return f"{self.title}"


    class Meta:
        ordering = ['-date_updated', '-date_created']
        verbose_name_plural = 'Diaries'

