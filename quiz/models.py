from django.db import models
from django.contrib.auth.models import User

#from ckeditor.fields import RichTextField
# Create your models here.

class Answer(models.Model):
    answer_text = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.answer_text}"

class Question(models.Model):
    question_text = models.CharField(max_length=900)
    answers = models.ManyToManyField(Answer)
    points = models.PositiveIntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.question_text}"

class Quizzes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)
    questions = models.ManyToManyField(Question)
    attempts = models.PositiveIntegerField(default=0, null=True, blank=True)
    total_average_score = models.PositiveIntegerField(default=0, null=True, blank=True)
    average_score = models.FloatField(default=0, null=True, blank=True)

    class Meta:
        ordering = ['-date', 'attempts']
        verbose_name_plural = 'Quizzes'

        
    def __str__(self):
        return f"{self.title}"

class Attempter(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quizzes, on_delete=models.CASCADE)
    score = models.PositiveIntegerField()
    completed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} | {self.quiz}"

class Attempt(models.Model):
    quiz = models.ForeignKey(Quizzes, on_delete=models.CASCADE)
    attempter = models.ForeignKey(Attempter, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.quiz.title}"


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    bio = models.TextField(max_length=1000)
    date_of_birth = models.DateField(null=True, blank=True)
    quizAttempted = models.ForeignKey(Quizzes, on_delete=models.CASCADE, related_name="quizAttempted", null=True, blank=True)
    quizCreated = models.ForeignKey(Quizzes, on_delete=models.CASCADE, related_name="quizCreated", null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}"

    