
from django import forms
from .models import QFourChoicesQuestion, QTrueOrFalseQuestion
from quiz.models import Category


class NewCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('title',)


class NewQFourChoicesQuestionForm(forms.ModelForm):

    class Meta:
        model = QFourChoicesQuestion
        fields = '__all__'
        exclude = ('user', 'form')



class NewQTrueOrFalseQuestionForm(forms.ModelForm):

    class Meta:
        model = QTrueOrFalseQuestion
        fields = '__all__'
        exclude = ('user', 'form','answer1', 'answer2',)


