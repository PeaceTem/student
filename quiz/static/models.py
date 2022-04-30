from django.db import models
from django.contrib.auth.models import User
from datetime import date, datetime
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _



from question.models import TrueOrFalseQuestion, FourChoicesQuestion

from category.models import Category

from PIL import Image

from random import shuffle


from .managers import QuizManager

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
# """
# class FourChoicesQuestion(models.Model):
#     ANSWER_CHOICES = (
#         ('answer1', 'answer1'),
#         ('answer2', 'answer2'),
#         ('answer3', 'answer3'),
#         ('answer4', 'answer4'),
#     )

#     SCORE_CHOICES = zip( range(5,0, -1), range(5,0, -1) )
#     DURATION_CHOICES = zip( range(15,181, 5), range(15,181, 5) )

#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     index = models.PositiveSmallIntegerField(default=1)
#     form = models.CharField(max_length=30, default='fourChoicesQuestion')
#     date_created = models.DateTimeField(auto_now_add=True)
#     question = models.TextField(max_length=1000)
#     answer1 = models.CharField(max_length=200)
#     answer2 = models.CharField(max_length=200)
#     answer3 = models.CharField(max_length=200)
#     answer4 = models.CharField(max_length=200)
#     correct = models.CharField(max_length=100, choices=ANSWER_CHOICES)
#     solution = models.TextField(max_length=500, default='The creator of this quiz did not provide any solution for this question!')
#     points = models.PositiveSmallIntegerField(choices=SCORE_CHOICES, default=1)
#     duration = models.PositiveSmallIntegerField(choices=DURATION_CHOICES, default=20)
#     attempts = models.PositiveIntegerField(default=0)
#     answer1NumberOfTimesTaken = models.PositiveIntegerField(default=0)
#     answer2NumberOfTimesTaken = models.PositiveIntegerField(default=0)
#     answer3NumberOfTimesTaken = models.PositiveIntegerField(default=0)
#     answer4NumberOfTimesTaken = models.PositiveIntegerField(default=0)
#     shuffleAnswers = models.BooleanField(default=False)




#     @property
#     def shuffle_answers(self):
#         _newlist = [1,2,3,4]
#         if self.shuffleAnswers:
#             shuffle(_newlist)
#         return _newlist




#     @property
#     def get_percentage_chosen_of_answer1(self):
#         total_question_attempts = self.attempts
#         _answer1 = self.answer1NumberOfTimesTaken
#         result = round((_answer1/total_question_attempts) * 100,2)

#         return f"{result}%"



#     @property
#     def get_percentage_chosen_of_answer2(self):
#         total_question_attempts = self.attempts
#         _answer2 = self.answer2NumberOfTimesTaken
#         result = round((_answer2/total_question_attempts) * 100,2)

#         return f"{result}%"



#     @property
#     def get_percentage_chosen_of_answer3(self):
#         total_question_attempts = self.attempts
#         _answer3 = self.answer3NumberOfTimesTaken
#         result = round((_answer3/total_question_attempts) * 100,2)

#         return f"{result}%"


#     @property
#     def get_percentage_chosen_of_answer4(self):
#         total_question_attempts = self.attempts
#         _answer4 = self.answer4NumberOfTimesTaken
#         result = round((_answer4/total_question_attempts) * 100,2)

#         return f"{result}%"




#     def getAnswer(self, value, *args, **kwargs):
#         if value == 'answer1':
#             return self.answer1
#         elif value == 'answer2':
#             return self.answer2
#         elif value == 'answer3':
#             return self.answer3
#         elif value == 'answer4':
#             return self.answer4
#         else:
#             return None




#     def __str__(self):
#         return f"{self.question}"




# class TrueOrFalseQuestion(models.Model):
#     ANSWER_CHOICES = (
#         ('True', 'True'),
#         ('False', 'False'),
#     )


#     DURATION_CHOICES = zip( range(15,181, 5), range(15,181, 5) )
#     SCORE_CHOICES = zip( range(5,0, -1), range(5,0, -1) )
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     index = models.PositiveSmallIntegerField(default=1)
#     form = models.CharField(max_length=20, default='trueOrFalseQuestion')
#     question = models.TextField(max_length=500)
#     answer1 = models.CharField(max_length=20, default='True')
#     answer2 = models.CharField(max_length=20, default='False')
#     correct = models.CharField(max_length=100, choices=ANSWER_CHOICES)
#     solution = models.TextField(max_length=500, default='The creator of this quiz did not provide any solution for this question!')
#     points = models.PositiveSmallIntegerField(choices=SCORE_CHOICES, default=1)
#     duration = models.PositiveSmallIntegerField(choices=DURATION_CHOICES, default=20)
#     attempts = models.PositiveIntegerField(default=0)
#     answer1NumberOfTimesTaken = models.PositiveIntegerField(default=0)
#     answer2NumberOfTimesTaken = models.PositiveIntegerField(default=0)


#     @property
#     def get_percentage_chosen_of_answer1(self):
#         total_question_attempts = self.attempts
#         _answer1 = self.answer1NumberOfTimesTaken
#         result = round((_answer1/total_question_attempts) * 100,2)

#         return f"{result}%"


#     @property
#     def get_percentage_chosen_of_answer2(self):
#         total_question_attempts = self.attempts
#         _answer2 = self.answer2NumberOfTimesTaken
#         result = round((_answer2/total_question_attempts) * 100,2)

#         return f"{result}%"







#     def getAnswer(self, value, *args, **kwargs):
#         if value == 'answer1':
#             return self.answer1
#         elif value == 'answer2':
#             return self.answer2
#         else:
#             return None




#     def __str__(self):
#         return f"{self.question}"



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
    shuffleQuestions = models.BooleanField(default=False)
    attempts = models.PositiveIntegerField(default=0)
    gross_average_score = models.PositiveIntegerField(default=0)
    average_score = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    public = models.BooleanField(default=True)
    categories = models.ManyToManyField(Category, blank=True,
        related_name='categories', related_query_name='categories')
    #duration and each quiz is in minutes, and it overrides the duration of all the questions
    duration_in_minutes = models.PositiveSmallIntegerField(choices=DURATION_CHOICES, default=3)
    solution_quality = models.IntegerField(default=0)
    likes = models.ManyToManyField(User, default=None, blank=True, related_name='likes')
    likeCount = models.PositiveIntegerField(default=0)
    solution_validators = models.ManyToManyField(User,  blank=True, related_name='quiz_solution_validators')
    age_from = models.PositiveSmallIntegerField(null=True, verbose_name=_('Minimum Age Of Quiz Takers'))
    age_to = models.PositiveSmallIntegerField(null=True, verbose_name=_('Maximum Age Of Quiz Takers'))


    objects = QuizManager()


    def clean(self):
        a1 = self.age_from
        a2 = self.age_to
        if a1 is not None and a2 is not None and a1 > a2:
            raise ValidationError(_('minimum age should be less than or equal too maximum age'))

            if a2 > 65:
                raise ValidationError(_("The maximum age can be less than  or equal to 65"))

        super().clean()
    


    @property
    def last_update(self):
        days_length = date.today() - self.date_updated.date()
        days_length_shrink = str(days_length).split(',', 1)[0]
        return days_length_shrink


    @property
    def when_created(self):
        days_length = date.today() - self.date.date()
        print(days_length)
        
        try:
            days_length_shrink = str(days_length).split(',', 1)[0]
            days_length_shrink = days_length_shrink[:len(days_length_shrink) - 4]

            days_length_shrink = int(days_length_shrink)

            if days_length_shrink > 364:
                days_length_shrink = days_length_shrink // 365
                if days_length_shrink < 2:
                    return f"{str(days_length_shrink)} year"
                return f"{str(days_length_shrink)} years"
            elif days_length_shrink > 29:
                days_length_shrink = days_length_shrink // 30
                if days_length_shrink < 2:
                    return f"{str(days_length_shrink)} month"
                return f"{str(days_length_shrink)} months"
            elif days_length_shrink > 6:
                days_length_shrink = days_length_shrink // 7
                if days_length_shrink < 2:
                    return f"{str(days_length_shrink)} week"
                return f"{str(days_length_shrink)} weeks"
            if days_length_shrink < 2:
                    return f"{str(days_length_shrink)} day"
            return f"{str(days_length_shrink)} days"
        except:
            return f"0 days"

    class Meta:
        ordering = ['-date']
        verbose_name_plural = 'Quizzes'

        
    def __str__(self):
        return f"{self.title}"





class QuizLink(models.Model):
    quiz = models.OneToOneField(Quiz, on_delete=models.CASCADE, related_name='quizlink', editable=False)
    name = models.CharField(max_length=80)
    link = models.URLField()
    description = models.TextField(max_length=200)
    ban = models.BooleanField(default=False)
    reportCount = models.PositiveSmallIntegerField(default=0)
    clicks = models.PositiveIntegerField(default=0)
    reporters = models.ManyToManyField(User, blank=True)





class Attempter(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.PositiveSmallIntegerField(default=0)
    percentage = models.FloatField(default=0.0)



    class Meta:
        ordering = ['-percentage', '-score']

    @property
    def get_percentage(self):
        return f"{self.percentage}%"


    


    def __str__(self):
        return f"{self.user.username}"

    # check if the attempter has not been created before creating another instance of attempter



# class Person(models.Model):
#     name = CharField(max_length=100)
#     age = supply property




# class Author(models.Model):
#     person = supply the property


# class Book(models.Model):
#     name = CharField(max_length=100)

#     published_date = supply the property
#     # a book has many readers and may have many authors
#     readers = supply the property
#     authors = supply the property
#     category = supply field

# class Category(models.Model):
#     name = models.CharField(max_length=100, unique=True, help_text="Each category is unique!")
#     # register by a person
#     registered_by = supply the field to this property of the object category.
#     date_created = supply the field to this property of the object category.




# class Library(models.Model):
#     name = models.CharField(max_length=100)
#     librarian = supply field
#     books = supply field

    # def save(self, *args, **kwargs):
    #     #use the pre_save signal to handle this task.
    #     # change this at property
    #     print('printing')

    #     if self.age_to is None and self.age_from is None:
    #         age = None
    #         try:
    #             age = self.user.profile.date_of_birth
    #             age = date.today() - age
    #             age = age.days // 365
    #             print(age)
    #             if age < 65:
    #                 print(age)
    #                 self.age_from = age - 2
                    
    #                 self.age_to = age
    #                 super().save(*args, **kwargs)
    #                 print('saved')
    #         except:
    #             pass
    #     super().save(*args, **kwargs)