from django.urls import path
from .views import CustomLoginView, RegisterPage, ProfilePage, ProfileCreationPage
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('register/', RegisterPage.as_view(), name='register'),
    path('login/', CustomLoginView, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    #reset password
    path('reset_password/', auth_views.PasswordResetView.as_view(),
     name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(),
     name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
     name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(),
     name='reset_password_complete'),

    # profile
    path('profile/', ProfilePage, name='profile'),
    path('edit_profile/', ProfileCreationPage, name='edit_profile'),

]
"""template_name='core/password_reset.html'"""
"""template_name='core/reset_password_sent.html'"""
"""template_name='core/password_reset_form.html'"""

"""template_name='core/password_reset_complete.html'"""

