from django.urls import path 
from .views import DiaryList, DiaryCreate, DiaryUpdate, DiaryDetail



urlpatterns = [
    path('', DiaryList.as_view(), name='diaries'),
    path('diary-create/', DiaryCreate.as_view(), name='diary-create'),
    path('diary-update/<str:pk>', DiaryUpdate.as_view(), name='diary-update'),
    path('diary-detail/<str:pk>', DiaryDetail.as_view(), name='diary-detail'),
]