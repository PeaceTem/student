from django.urls import path
from .views import QuizList, RegisterPage, CustomLoginView, NewQuiz, NewQuestion, QuizDetail, TakeQuiz, SubmitAttempt

from django.contrib.auth.views import LogoutView

app_name = 'quiz'
urlpatterns = [
    path('', QuizList, name='quizzes'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='quiz:login'), name='logout'),


    path('newquiz/', NewQuiz, name='new-quiz'),
    path('<quiz_id>/newquestion', NewQuestion, name='new-question'),
    path('<quiz_id>/', QuizDetail, name='quiz-detail'),
    path('<quiz_id>/take', TakeQuiz, name='take-quiz'),
    path('<quiz_id>/take/submit', SubmitAttempt, name='submit-quiz'),
]

