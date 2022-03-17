from django.urls import path
from . import views


app_name = 'leaderboard'


urlpatterns = [

    path('streak/', views.StreakLeaderBoard, name='streak'),
    path('wealth/', views.WealthLeaderBoard, name='wealth'),

]

