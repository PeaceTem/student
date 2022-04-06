from django import forms

from .models import Profile, Link




class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)


    
class ProfileCreationForm(forms.ModelForm):
    date_of_birth = forms.DateTimeField(input_formats=['%d/%m/%Y'])
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user', 'date_updated', 'coins', 'link', 'streak', 'code', 'referrer', 'views', 'picture', 'refercount', 'slug', 'relevance', 'categories', 'quizTaken', 'trueOrFalseQuestionsMissed', 'fourChoicesQuestionsMissed', 'trueOrFalseQuestionsTaken', 'fourChoicesQuestionsTaken', 'quizAvgScore', 'questionAvgScore', 'quizAttempts', 'questionAttempts', 'likes', 'quizzes',]


class NewLinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = '__all__'
        exclude = ('profile', 'clicks')