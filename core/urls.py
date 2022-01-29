from django.urls import path
from .views import CustomLoginView, RegisterPage
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/', RegisterPage.as_view(), name='register'),
    path('login/', CustomLoginView, name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]
