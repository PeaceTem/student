from django.urls import path


from . import views



app_name = 'question'

 
urlpatterns = [
    #question
    path('new-question/', views.QuestionCreate, name='new-question'),

    path('create-question/four-choices/', views.FourChoicesQuestionCreate, name='fourChoicesQuestion'),
    path('edit-question/four-choices/<str:question_id>/', views.FourChoicesQuestionUpdate, name='edit-fourChoicesQuestion'),


    path('create-question/true-or-false/', views.TrueOrFalseQuestionCreate, name='trueOrFalseQuestion'),
    path('edit-question/true-or-false/<str:question_id>/', views.TrueOrFalseQuestionUpdate, name='edit-trueOrFalseQuestion'),

    # answer question
    path('take/', views.AnswerQuestion, name='answer-question'),
    path('submit/', views.SubmitQuestion, name='submit-question'),

]





# from .views import (GeneratePDF, QuizList, QuizDetail, QuizCreate, QuizUpdate, DeleteQuiz, CategoryCreate, QuestionCreate,
#  FourChoicesQuestionCreate, FourChoicesQuestionUpdate, TrueOrFalseQuestionCreate, TrueOrFalseQuestionUpdate, TakeQuiz, SubmitQuiz)

