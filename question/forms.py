
from django import forms
from .models import QFourChoicesQuestion, QTrueOrFalseQuestion
from quiz.models import Category

class NewQFourChoicesQuestionForm(forms.ModelForm):

    class Meta:
        model = QFourChoicesQuestion
        fields = '__all__'
        exclude = ('user', 'form', 'categories', 'attempts', 'avgScore',  'solution_quality', 'solution_validators',)



class NewQTrueOrFalseQuestionForm(forms.ModelForm):

    class Meta:
        model = QTrueOrFalseQuestion
        fields = '__all__'
        exclude = ('user', 'form','answer1', 'answer2', 'categories', 'attempts', 'avgScore',  'solution_quality', 'solution_validators',)




class QuizGeneratorForm(forms.Form):
    duration_in_minutes = forms.IntegerField()
    number_of_questions = forms.IntegerField()
    
    