from django import forms

from .models import Profile




class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)


    
class ProfileCreationForm(forms.ModelForm):
    date_of_birth = forms.DateTimeField(input_formats=['%d/%m/%Y'])
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user', 'date_updated', 'coins', 'streak', 'code', 'referrer']

