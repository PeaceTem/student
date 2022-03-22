from django import forms


from django import forms
from .models import Quiz, Category, FourChoicesQuestion, TrueOrFalseQuestion

class NewQuizForm(forms.ModelForm):

    class Meta:
        model = Quiz
        fields = '__all__'
        exclude = ('user','date', 'date_updated', 'likes', 'categories', 'fourChoicesQuestions', 'trueOrFalseQuestions', 'lastQuestionIndex', 'questionLength', 'totalScore', 'attempts','gross_average_score','average_score', 'public',)
      


class NewCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('title',)


class NewFourChoicesQuestionForm(forms.ModelForm):

    class Meta:
        model = FourChoicesQuestion
        fields = '__all__'
        exclude = ('user',  'index', 'form')



class NewTrueOrFalseQuestionForm(forms.ModelForm):

    class Meta:
        model = TrueOrFalseQuestion
        fields = '__all__'
        exclude = ('user', 'index', 'form','answer1', 'answer2',)


