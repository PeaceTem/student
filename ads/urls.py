from django.urls import path
from . import views

app_name='ads'

urlpatterns = [
    path('postAd/', views.PostAdView, name='postAd'),
    path('postAd/click/<int:post_id>/', views.PostAdClick, name='post-click'),
]