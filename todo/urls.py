from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete

app_name = 'todo'


urlpatterns = [
    path('', TaskList, name='tasks'),
    path('task/<str:pk>/', TaskDetail, name='task'),
    path('task-create/', TaskCreate, name='task-create'),
    path('task-update/<str:pk>', TaskUpdate, name='task-update'),
    path('task-delete/<str:pk>', TaskDelete.as_view(), name='task-delete'),
]