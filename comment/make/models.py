from django.db import models
from django.contrib.auth.models import User
# from quiz.models import Quiz
# Create your models here.


class Comment(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    text = models.CharField(max_length=200)




class QuizComment(models.Model):
    # quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, null=True)
    comments = models.ManyToManyField(Comment, blank=True)

    def __str__(self):
        return f"{self.quiz}"
