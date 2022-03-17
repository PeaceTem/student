# from django.db import models
# from django.contrib.auth.models import User
# from datetime import date, datetime
# from django.utils import timezone
# from django.contrib.postgres.fields import ArrayField
# from PIL import Image


# from quiz.models import FourChoicesQuestion, TrueOrFalseQuestion, Category
# # Create your models here.





# class DraftFourChoicesQuestion(models.Model):
#     ANSWER_CHOICES = (
#         ('answer1', 'answer1'),
#         ('answer2', 'answer2'),
#         ('answer3', 'answer3'),
#         ('answer4', 'answer4'),
#     )

#     SCORE_CHOICES = zip( range(5,0, -1), range(5,0, -1) )
#     DURATION_CHOICES = zip( range(15,181, 5), range(15,181, 5) )

#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     question_text = models.TextField(max_length=500, null=True, blank=True)
#     thumbnail = models.ImageField(upload_to='images/', blank=True, null=True)
#     answer1 = models.CharField(max_length=200, null=True, blank=True)
#     answer2 = models.CharField(max_length=200, null=True, blank=True)
#     answer3 = models.CharField(max_length=200, null=True, blank=True)
#     answer4 = models.CharField(max_length=200, null=True, blank=True)
#     correct = models.CharField(max_length=100, choices=ANSWER_CHOICES, null=True, blank=True)
#     solution = models.TextField(max_length=500, null=True, blank=True)
#     solutionThumbnail = models.ImageField(upload_to='images/',  blank=True, null=True)
#     points = models.PositiveSmallIntegerField(choices=SCORE_CHOICES, default=1)
#     duration = models.PositiveSmallIntegerField(choices=DURATION_CHOICES, default=15)



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
#         return f"{self.question_text}"




# class DraftTrueOrFalseQuestion(models.Model):
#     ANSWER_CHOICES = (
#         ('True', 'True'),
#         ('False', 'False'),
#     )


#     DURATION_CHOICES = zip( range(15,181, 5), range(15,181, 5) )
#     SCORE_CHOICES = zip( range(5,0, -1), range(5,0, -1) )
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     question_text = models.CharField(max_length=200, null=True, blank=True)
#     thumbnail = models.ImageField(upload_to='images/',  blank=True, null=True)
#     answer1 = models.CharField(max_length=20, default='True')
#     answer2 = models.CharField(max_length=20, default='False')
#     correct = models.CharField(max_length=100, choices=ANSWER_CHOICES, null=True, blank=True)
#     solution = models.TextField(max_length=500, null=True, blank=True)
#     solutionThumbnail = models.ImageField(upload_to='images/',  blank=True, null=True)
#     points = models.PositiveSmallIntegerField(choices=SCORE_CHOICES, default=1)
#     duration = models.PositiveSmallIntegerField(choices=DURATION_CHOICES, default=20)

#     def getAnswer(self, value, *args, **kwargs):
#         if value == 'answer1':
#             return self.answer1
#         elif value == 'answer2':
#             return self.answer2
#         else:
#             return None




#     def __str__(self):
#         return f"{self.question_text}"








# class DraftQuiz(models.Model):

#     DURATION_CHOICES = zip( range(1,61), range(1,61) )
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
#     title = models.CharField(max_length=200, null=True, blank=True)
#     description = models.TextField(max_length=1000, null=True, blank=True)
#     date = models.DateTimeField(auto_now_add=True)
#     date_updated = models.DateTimeField(auto_now=True, null=True, blank=True)
#     fourChoicesQuestions = models.ManyToManyField(FourChoicesQuestion, related_name='draft_fourChoicesQuestions',
#         related_query_name='draft_fourChoicesQuestions' , blank=True)
#     trueOrFalseQuestions = models.ManyToManyField(TrueOrFalseQuestion, related_name='draft_trueOrFalseQuestions',
#         related_query_name='draft_trueOrFalseQuestions', blank=True)

#     lastQuestionIndex = models.PositiveSmallIntegerField(default=0)
#     questionLength = models.PositiveSmallIntegerField(default=0)
#     totalScore = models.PositiveSmallIntegerField(default=0)
#     shuffleable = models.BooleanField(default=False)
#     attempts = models.PositiveIntegerField(default=0)
#     gross_average_score = models.PositiveIntegerField(default=0)
#     average_score = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
#     public = models.BooleanField(default=True)
#     thumbnail = models.ImageField(upload_to='images/', blank=True, null=True)
#     categories = models.ManyToManyField(Category,
#         related_name='draft_categories', related_query_name='draft_categories', blank=True)
#     #duration and each quiz is in minutes, and it overrides the duration of all the questions
#     duration = models.PositiveSmallIntegerField(choices=DURATION_CHOICES, null=True, blank=True)



#     def save(self, *args, **kwargs):
#         #use the pre_save signal to handle this task.
#         super().save(*args, **kwargs)
#         if self.thumbnail:
#             img = Image.open(self.thumbnail)
#             if img.height > 300 or img.width > 300:
#                 output_size = (100,100)
#                 img.thumbnail(output_size)
#                 img.save(self.thumbnail.path)



#     class Meta:
#         ordering = ['-date', 'attempts']
#         verbose_name_plural = 'DraftQuizzes'

        
#     def __str__(self):
#         return f"{self.title}"




