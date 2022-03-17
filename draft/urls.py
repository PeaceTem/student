# from django.urls import path 
# from . import views

# app_name = 'draft'


# urlpatterns = [
#     path('create-quiz/', views.DraftQuizCreate, name='quiz-create'),
#     path('edit-quiz/<str:quiz_id>/', views.DraftQuizUpdate, name='quiz-update'),
#     path('delete-quiz/<quiz_id>', views.DraftDeleteQuiz, name='delete-quiz'),

#     #convert to Live
#     path('convert/<str:quiz_id>/', views.ConvertDraftQuizToLive, name='quiz-convert'),

#     #question
#     path('<str:quiz_id>/new-question/', views.DraftQuestionCreate, name='new-question'),

#     path('<str:quiz_id>/create-question/four-choices/', views.DraftFourChoicesQuestionCreate, name='fourChoicesQuestion'),
#     path('<str:quiz_id>/edit-question/four-choices/<str:question_id>/', views.DraftFourChoicesQuestionUpdate, name='edit-fourChoicesQuestion'),


#     path('<str:quiz_id>/create-question/true-or-false/', views.DraftTrueOrFalseQuestionCreate, name='trueOrFalseQuestion'),
#     path('<str:quiz_id>/edit-question/true-or-false/<str:question_id>/', views.DraftTrueOrFalseQuestionUpdate, name='edit-trueOrFalseQuestion'),
# ]