from django.db import models
from django.contrib.auth.models import User
from datetime import date, datetime
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField
from PIL import Image


# Create your models here.

"""
Add the documentation to all the objects in the file.
This attempt is just for clarification in the process of making the whole app.

Control the redirect of tothex.org to tothex.org/quiz/
Create a QuizTemplate that all other types of quiz, like draft and scheduled, will inherit from.
Add the solution field to questions from the beginning of everything as part of the field of the different questions presented here.
Delete all the migrations files and dbsqlite3

Use Try, Except Block extensively in your views.
"""

"""
Users have the option to choose an answer from four different options
The index field is just the for ordering the questions in quiz 
The duration is in sec

Use Try except block thoroughly
"""
class FourChoicesQuestion(models.Model):
    ANSWER_CHOICES = (
        ('answer1', 'answer1'),
        ('answer2', 'answer2'),
        ('answer3', 'answer3'),
        ('answer4', 'answer4'),
    )

    SCORE_CHOICES = zip( range(5,0, -1), range(5,0, -1) )
    DURATION_CHOICES = zip( range(15,181, 5), range(15,181, 5) )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    index = models.PositiveSmallIntegerField(default=1)
    form = models.CharField(max_length=30, default='fourChoicesQuestion')
    question_text = models.TextField(max_length=500)
    answer1 = models.CharField(max_length=200)
    answer2 = models.CharField(max_length=200)
    answer3 = models.CharField(max_length=200)
    answer4 = models.CharField(max_length=200)
    correct = models.CharField(max_length=100, choices=ANSWER_CHOICES)
    solution = models.TextField(max_length=500, null=True, blank=True)
    points = models.PositiveSmallIntegerField(choices=SCORE_CHOICES, default=1)
    duration = models.PositiveSmallIntegerField(choices=DURATION_CHOICES, default=15)



    def getAnswer(self, value, *args, **kwargs):
        if value == 'answer1':
            return self.answer1
        elif value == 'answer2':
            return self.answer2
        elif value == 'answer3':
            return self.answer3
        elif value == 'answer4':
            return self.answer4
        else:
            return None




    def __str__(self):
        return f"{self.question_text}"




class TrueOrFalseQuestion(models.Model):
    ANSWER_CHOICES = (
        ('True', 'True'),
        ('False', 'False'),
    )


    DURATION_CHOICES = zip( range(15,181, 5), range(15,181, 5) )
    SCORE_CHOICES = zip( range(5,0, -1), range(5,0, -1) )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    index = models.PositiveSmallIntegerField(default=1)
    form = models.CharField(max_length=20, default='trueOrFalseQuestion')
    question_text = models.CharField(max_length=200)
    answer1 = models.CharField(max_length=20, default='True')
    answer2 = models.CharField(max_length=20, default='False')
    correct = models.CharField(max_length=100, choices=ANSWER_CHOICES)
    solution = models.TextField(max_length=500, null=True, blank=True)
    points = models.PositiveSmallIntegerField(choices=SCORE_CHOICES, default=1)
    duration = models.PositiveSmallIntegerField(choices=DURATION_CHOICES, default=20)

    def getAnswer(self, value, *args, **kwargs):
        if value == 'answer1':
            return self.answer1
        elif value == 'answer2':
            return self.answer2
        else:
            return None




    def __str__(self):
        return f"{self.question_text}"




"""
Perform some calculations on the number of times the category has being taken.
and the relevance

Add the number of questions with this category
"""

class Category(models.Model):
    title = models.CharField(max_length=50, unique=True)
    registered_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    relevance = models.IntegerField(default=0)
    number_of_quizzes = models.PositiveIntegerField(default=0)
    number_of_questions = models.PositiveIntegerField(default=0)
    # this represent the number of times the quizzes affiliated with this category were taken
    quiz_number_of_times_taken = models.PositiveIntegerField(default=0)
    question_number_of_times_taken = models.PositiveIntegerField(default=0)
    date_registered = models.DateTimeField(auto_now_add=True)
    #add images to this Also
    thumbnail = models.ImageField(upload_to='images/',  blank=True, null=True)

    class Meta:
        verbose_name_plural='Categories'

    def __str__(self):
        return f"category | {self.title}"



class Quiz(models.Model):

    DURATION_CHOICES = zip( range(1,61), range(1,61) )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True, null=True, blank=True)
    fourChoicesQuestions = models.ManyToManyField(FourChoicesQuestion, related_name='fourChoicesQuestions',
        related_query_name='fourChoicesQuestions' , blank=True)
    trueOrFalseQuestions = models.ManyToManyField(TrueOrFalseQuestion, related_name='trueOrFalseQuestions',
        related_query_name='trueOrFalseQuestions', blank=True)

    lastQuestionIndex = models.PositiveSmallIntegerField(default=0)
    questionLength = models.PositiveSmallIntegerField(default=0)
    totalScore = models.PositiveSmallIntegerField(default=0)
    shuffleable = models.BooleanField(default=False)
    attempts = models.PositiveIntegerField(default=0)
    gross_average_score = models.PositiveIntegerField(default=0)
    average_score = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    public = models.BooleanField(default=True)
    categories = models.ManyToManyField(Category, blank=True,
        related_name='categories', related_query_name='categories')
    #duration and each quiz is in minutes, and it overrides the duration of all the questions
    duration = models.PositiveSmallIntegerField(choices=DURATION_CHOICES, null=True, blank=True)

    likes = models.ManyToManyField(User, default=None, blank=True, related_name='likes')


    @property
    def num_likes(self):
        return self.likes.all().count()




    
    # def save(self, *args, **kwargs):
    #     #use the pre_save signal to handle this task.
    #     super().save(*args, **kwargs)
    #     if self.thumbnail:
    #         img = Image.open(self.thumbnail)
    #         if img.height > 300 or img.width > 300:
    #             output_size = (100,100)
    #             img.thumbnail(output_size)
    #             img.save(self.thumbnail.path)



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


