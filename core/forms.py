from django import forms

from .models import Profile

class ProfileCreationForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user', 'quizAttempted', 'quizCreated', 'date_joined', 'date_updated', 'streak', 'diaries', 'tasks', 'code', 'referrer']