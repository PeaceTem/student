from django.urls import path


from . import views



app_name = 'quiz'

 
urlpatterns = [
    path('', views.QuizList, name='quizzes'),
    path('following-quizzes/', views.FollowerQuizList, name='following-quizzes'),
    path('my-quizzes/', views.MyQuizList, name='my-quizzes'),
    path('detail/<str:quiz_id>/<str:ref_code>', views.QuizDetail, name='quiz-detail'),
    path('create-quiz/', views.QuizCreate, name='quiz-create'),
    path('create/', views.CreateObject, name='object-create'),
    path('edit-quiz/<str:quiz_id>/', views.QuizUpdate, name='quiz-update'),
    path('delete-quiz/<quiz_id>', views.DeleteQuiz, name='delete-quiz'),
    path('delete-question/<str:quiz_id>/<str:question_form>/<str:question_id>/', views.DeleteQuestion, name='delete-question'),

    #like post
    path('like/', views.PostLike, name ='post-like'),

    #category
    path('create_category/<str:quiz_id>/', views.CategoryCreate, name='category-create'),

    #question
    path('<str:quiz_id>/new-question/', views.QuestionCreate, name='new-question'),

    path('<str:quiz_id>/create-question/four-choices/', views.FourChoicesQuestionCreate, name='fourChoicesQuestion'),
    path('<str:quiz_id>/edit-question/four-choices/<str:question_id>/', views.FourChoicesQuestionUpdate, name='edit-fourChoicesQuestion'),


    path('<str:quiz_id>/create-question/true-or-false/', views.TrueOrFalseQuestionCreate, name='trueOrFalseQuestion'),
    path('<str:quiz_id>/edit-question/true-or-false/<str:question_id>/', views.TrueOrFalseQuestionUpdate, name='edit-trueOrFalseQuestion'),
    #takequiz

    path('<str:quiz_id>/take/', views.TakeQuiz, name='take-quiz'),
    path('<str:quiz_id>/submit/<str:ref_code>', views.SubmitQuiz, name='submit-quiz'),

    #pdf generation
    path('<str:quiz_id>/pdf/', views.GeneratePDF.as_view(), name='quiz-pdf'),
]
# from .views import (GeneratePDF, QuizList, QuizDetail, QuizCreate, QuizUpdate, DeleteQuiz, CategoryCreate, QuestionCreate,
#  FourChoicesQuestionCreate, FourChoicesQuestionUpdate, TrueOrFalseQuestionCreate, TrueOrFalseQuestionUpdate, TakeQuiz, SubmitQuiz)