from django.urls import path
from .views import QuizList, NewQuiz, UpdateQuiz, DeleteQuiz, NewQuestion, QuizDetail, TakeQuiz, SubmitAttempt, QuizPdf

from django.contrib.auth.views import LogoutView

app_name = 'quiz'
urlpatterns = [
    path('', QuizList, name='quizzes'),
    path('newquiz/', NewQuiz, name='new-quiz'),
    path('update-quiz/<quiz_id>', UpdateQuiz, name='update-quiz'),
    path('delete-quiz/<quiz_id>', DeleteQuiz, name='delete-quiz'),
    path('<quiz_id>/newquestion/', NewQuestion, name='new-question'),
    path('<quiz_id>/', QuizDetail, name='quiz-detail'),
    path('<quiz_id>/take/', TakeQuiz, name='take-quiz'),
    path('<quiz_id>/take/submit/', SubmitAttempt, name='submit-quiz'),
    path('<quiz_id>/pdf/', QuizPdf, name='quiz-pdf'),

]

