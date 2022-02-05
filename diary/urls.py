from django.urls import path 
from .views import DiaryList, DiaryCreate, DiaryUpdate, DiaryDetail

app_name = 'diary'


urlpatterns = [
    path('', DiaryList, name='diaries'),
    path('diary-create/', DiaryCreate, name='diary-create'),
    path('diary-update/<str:pk>', DiaryUpdate, name='diary-update'),
    path('diary-detail/<str:pk>', DiaryDetail, name='diary-detail'),
]