from django.db import models
from django.contrib.auth.models import User
from datetime import date

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
    shuffleable = models.BooleanField(default=False)


    @property
    def shuffle_answer(self):
        return self.answers.shuffle()


    def __str__(self):
        return f"{self.question_text}"

class Quizzes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True, null=True, blank=True)
    questions = models.ManyToManyField(Question)
    attempts = models.PositiveIntegerField(default=0, null=True, blank=True)
    total_average_score = models.PositiveIntegerField(default=0, null=True, blank=True)
    average_score = models.DecimalField(max_digits=5, decimal_places=2, default=0.00, null=True, blank=True)


    @property
    def last_update(self):
        days_length = date.today() - self.date_updated.date()
        days_length_shrink = str(days_length).split(',', 1)[0]
        return days_length_shrink


    @property
    def when_created(self):
        days_length = date.today() - self.date.date()
        days_length_shrink = str(days_length).split(',', 1)[0]
        return days_length_shrink


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


