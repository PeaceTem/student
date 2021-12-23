from django import forms
#from ckeditor.widgets import CKeditorWidget
from .models import Quizzes, Question, Answer

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
        


    