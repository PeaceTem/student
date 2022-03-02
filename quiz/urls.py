from django.urls import path

from .views import (GeneratePDF, QuizList, QuizDetail, QuizCreate, QuizUpdate, DeleteQuiz, CategoryCreate, QuestionCreate,
 FourChoicesQuestionCreate, FourChoicesQuestionUpdate, TrueOrFalseQuestionCreate, TrueOrFalseQuestionUpdate,
  TakeQuiz, SubmitQuiz)


app_name = 'quiz'

 
urlpatterns = [
    path('', QuizList, name='quizzes'),
    path('detail/<str:quiz_id>/', QuizDetail, name='quiz-detail'),
    path('create-quiz/', QuizCreate, name='quiz-create'),
    path('edit-quiz/<str:quiz_id>/', QuizUpdate, name='quiz-update'),
    path('delete-quiz/<quiz_id>', DeleteQuiz, name='delete-quiz'),

    #category
    path('create_category/<str:quiz_id>/', CategoryCreate, name='category-create'),

    #question
    path('quiz/<str:quiz_id>/new-question/', QuestionCreate, name='new-question'),

    path('quiz/<str:quiz_id>/create-question/four-choices/', FourChoicesQuestionCreate, name='fourChoicesQuestion'),
    path('quiz/<str:quiz_id>/edit-question/four-choices/<str:question_id>/', FourChoicesQuestionUpdate, name='edit-fourChoicesQuestion'),


    path('quiz/<str:quiz_id>/create-question/true-or-false/', TrueOrFalseQuestionCreate, name='trueOrFalseQuestion'),
    path('quiz/<str:quiz_id>/edit-question/true-or-false/<str:question_id>/', TrueOrFalseQuestionUpdate, name='edit-trueOrFalseQuestion'),
    #takequiz
    path('quiz/<str:quiz_id>/take/', TakeQuiz, name='take-quiz'),
    path('quiz/<str:quiz_id>/submit/', SubmitQuiz, name='submit-quiz'),

    #pdf generation
    # path('<quiz_id>/pdf/', GeneratePDF.as_view(), name='quiz-pdf'),


]
