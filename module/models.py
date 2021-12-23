from django.db import models
from django.contrib.auth.models import User

from quiz.models import Quizzes
# Create your models here.

class Module(models.Model):
    title = models.CharField(max_length=150)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='moduleUser')
    hours = models.PositiveIntegerField()
    quizzes = models.ManyToManyField(Quizzes)

    def __str__(self):
        return f'{self.title}'