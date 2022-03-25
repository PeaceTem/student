from django.urls import path


from . import views



app_name = 'question'

 
urlpatterns = [
    #question
    path('new-question/', views.QuestionCreate, name='new-question'),
    path('questions/', views.Question, name='questions'),
    path('my-questions/', views.MyQuestionList, name='my-questions'),

    path('create-question/four-choices/', views.FourChoicesQuestionCreate, name='fourChoicesQuestion'),
    path('edit-question/four-choices/<str:question_id>/', views.FourChoicesQuestionUpdate, name='edit-fourChoicesQuestion'),


    path('create-question/true-or-false/', views.TrueOrFalseQuestionCreate, name='trueOrFalseQuestion'),
    path('edit-question/true-or-false/<str:question_id>/', views.TrueOrFalseQuestionUpdate, name='edit-trueOrFalseQuestion'),

    path('category-create/<str:question_id>/', views.CategoryCreate, name='category-create'),

    path('question-delete/<str:question_form>/<str:question_id>', views.DeleteQuestion, name='delete-question'),

    # answer question
    path('take/', views.AnswerQuestion, name='answer-question'),
    path('submit/', views.SubmitQuestion, name='submit-question'),

]





# from .views import (GeneratePDF, QuizList, QuizDetail, QuizCreate, QuizUpdate, DeleteQuiz, CategoryCreate, QuestionCreate,
#  FourChoicesQuestionCreate, FourChoicesQuestionUpdate, TrueOrFalseQuestionCreate, TrueOrFalseQuestionUpdate, TakeQuiz, SubmitQuiz)

