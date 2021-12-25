from django import forms
#from ckeditor.widgets import CKeditorWidget
from .models import Quizzes, Question, Answer

"""class UserForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']
"""

class NewQuizForm(forms.ModelForm):
    
    class Meta:
        model = Quizzes
        fields = ['title', 'description']

class NewQuestionForm(forms.ModelForm):
    
    class Meta:
        model = Question
        fields = ['question_text', 'points']

class NewAnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['answer_text', 'is_correct']
        


    