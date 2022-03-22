from django.db import models
from django.contrib.auth.models import User
from quiz.models import Category

# Create your models here.
"""
User should be able to like this quiz

"""


class QFourChoicesQuestion(models.Model):
    ANSWER_CHOICES = (
        ('answer1', 'answer1'),
        ('answer2', 'answer2'),
        ('answer3', 'answer3'),
        ('answer4', 'answer4'),
    )

    SCORE_CHOICES = zip( range(5,0, -1), range(5,0, -1) )
    DURATION_CHOICES = zip( range(15,181, 5), range(15,181, 5) )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    form = models.CharField(max_length=30, default='fourChoicesQuestion')
    question_text = models.TextField(max_length=500)
    answer1 = models.CharField(max_length=200)
    answer2 = models.CharField(max_length=200)
    answer3 = models.CharField(max_length=200)
    answer4 = models.CharField(max_length=200)
    correct = models.CharField(max_length=100, choices=ANSWER_CHOICES)
    solution = models.TextField(max_length=500, null=True, blank=True)
    duration = models.PositiveSmallIntegerField(choices=DURATION_CHOICES, default=15)
    categories = models.ManyToManyField(Category, related_name='FourChoicesQuestioncategories', blank=True)
    attempts = models.IntegerField(default=0)
    avgScore = models.FloatField(default=0.0)



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




class QTrueOrFalseQuestion(models.Model):
    ANSWER_CHOICES = (
        ('True', 'True'),
        ('False', 'False'),
    )


    DURATION_CHOICES = zip( range(15,181, 5), range(15,181, 5) )
    SCORE_CHOICES = zip( range(5,0, -1), range(5,0, -1) )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    form = models.CharField(max_length=20, default='trueOrFalseQuestion')
    question_text = models.CharField(max_length=200)
    answer1 = models.CharField(max_length=20, default='True')
    answer2 = models.CharField(max_length=20, default='False')
    correct = models.CharField(max_length=100, choices=ANSWER_CHOICES)
    solution = models.TextField(max_length=500, null=True, blank=True)
    duration = models.PositiveSmallIntegerField(choices=DURATION_CHOICES, default=20)
    categories = models.ManyToManyField(Category, related_name='trueOrFalseQuestioncategories', blank=True)
    attempts = models.IntegerField(default=0)
    avgScore = models.FloatField(default=0.0)

    def getAnswer(self, value, *args, **kwargs):
        if value == 'answer1':
            return self.answer1
        elif value == 'answer2':
            return self.answer2
        else:
            return None




    def __str__(self):
        return f"{self.question_text}"

