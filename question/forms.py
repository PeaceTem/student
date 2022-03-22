
from django import forms
from .models import QFourChoicesQuestion, QTrueOrFalseQuestion
from quiz.models import Category

class NewQFourChoicesQuestionForm(forms.ModelForm):

    class Meta:
        model = QFourChoicesQuestion
        fields = '__all__'
        exclude = ('user', 'form', 'categories')



class NewQTrueOrFalseQuestionForm(forms.ModelForm):

    class Meta:
        model = QTrueOrFalseQuestion
        fields = '__all__'
        exclude = ('user', 'form','answer1', 'answer2', 'categories')


