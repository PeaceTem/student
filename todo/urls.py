from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete

app_name = 'todo'


urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('task/<str:pk>/', TaskDetail.as_view(), name='task'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-update/<str:pk>', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<str:pk>', TaskDelete.as_view(), name='task-delete'),
]