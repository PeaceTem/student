# from django.db import models

# # Create your models here.
# from django.contrib.auth.models import User
# from core.models import Profile, Streak
# from quiz.models import Quiz, Attempter, Attempt
# from todo.models import Task

# # Add all the analysis here
# # Starting from the each page counter, to the total page counter, to the daily active users,
# # to the monthly active users
# # Also add all the AI and ML models that will be incorporated in the quiz
# # Add the page counter for each user here


# class PageCounter(models.Model):
#     quizListPage = models.PositiveIntegerField(default=0)
#     quizDetailPage = models.PositiveIntegerField(default=0)
#     quizCreationPage = models.PositiveIntegerField(default=0)
#     quizTakenPage = models.PositiveIntegerField(default=0)
#     quizSubmitPage = models.PositiveIntegerField(default=0)
#     quizUpdatePage = models.PositiveIntegerField(default=0)
#     quizDeletePage = models.PositiveIntegerField(default=0)
#     questionCreationPage = models.PositiveIntegerField(default=0)
#     questionUpdatePage = models.PositiveIntegerField(default=0)
#     qustionDeletePage = models.PositiveIntegerField(default=0)
#     fourChoicesQuestionCreationPage = models.PositiveIntegerField(default=0)
#     fourChoicesQuestionUpdatePage = models.PositiveIntegerField(default=0)
#     fourChoicesQuestionDeletePage = models.PositiveIntegerField(default=0)
#     trueOrFalseQuestionCreationPage = models.PositiveIntegerField(default=0)
#     trueOrFalseQuestionUpdatePage = models.PositiveIntegerField(default=0)
#     trueOrFalseQuestionDeletePage = models.PositiveIntegerField(default=0)
#     pdfDownload = models.PositiveIntegerField(default=0)


#     class Meta:
#         verbose_name_plural = 'PageCounter'





# class UserPageCounter(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     quizListPage = models.PositiveIntegerField(default=0)
#     quizDetailPage = models.PositiveIntegerField(default=0)
#     quizCreationPage = models.PositiveIntegerField(default=0)
#     quizTakenPage = models.PositiveIntegerField(default=0)
#     quizSubmitPage = models.PositiveIntegerField(default=0)
#     quizUpdatePage = models.PositiveIntegerField(default=0)
#     quizDeletePage = models.PositiveIntegerField(default=0)
#     questionCreationPage = models.PositiveIntegerField(default=0)
#     questionUpdatePage = models.PositiveIntegerField(default=0)
#     qustionDeletePage = models.PositiveIntegerField(default=0)
#     fourChoicesQuestionCreationPage = models.PositiveIntegerField(default=0)
#     fourChoicesQuestionUpdatePage = models.PositiveIntegerField(default=0)
#     fourChoicesQuestionDeletePage = models.PositiveIntegerField(default=0)
#     trueOrFalseQuestionCreationPage = models.PositiveIntegerField(default=0)
#     trueOrFalseQuestionUpdatePage = models.PositiveIntegerField(default=0)
#     trueOrFalseQuestionDeletePage = models.PositiveIntegerField(default=0)
#     pdfDownload = models.PositiveIntegerField(default=0)

#     def __str__(self):
#         return f"{self.user.username}"


#     class Meta:
#         verbose_name_plural = 'UserPageCounter'






