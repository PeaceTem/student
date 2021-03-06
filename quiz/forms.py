from django import forms
from category.models import Category
from .models import Quiz, QuizLink
from question.models import FourChoicesQuestion, TrueOrFalseQuestion
class NewQuizForm(forms.ModelForm):

    class Meta:
        model = Quiz
        fields = '__all__'
        exclude = ('user','date', 'date_updated', 'likes', 'categories', 'fourChoicesQuestions', 'trueOrFalseQuestions', 'lastQuestionIndex', 'questionLength', 'totalScore', 'attempts','gross_average_score','average_score', 'public', 'solution_quality', 'solution_validators', 'likeCount', 'duration', 'relevance')
      

class NewFourChoicesQuestionForm(forms.ModelForm):

    class Meta:
        model = FourChoicesQuestion
        fields = '__all__'
        exclude = ('user',  'index', 'form', 'attempts', 'avgScore', 'answer1NumberOfTimesTaken', 'answer2NumberOfTimesTaken', 'categories', 'solution_quality', 'solution_validators' , 'answer3NumberOfTimesTaken', 'answer4NumberOfTimesTaken')



class NewTrueOrFalseQuestionForm(forms.ModelForm):

    class Meta:
        model = TrueOrFalseQuestion
        fields = '__all__'
        exclude = ('user', 'index', 'form','answer1', 'answer2', 'attempts',  'avgScore', 'answer1NumberOfTimesTaken', 'answer2NumberOfTimesTaken', 'solution_quality', 'categories', 'solution_validators')


class NewQuizLinkForm(forms.ModelForm):

    class Meta:
        model = QuizLink
        fields = '__all__'
        exclude =  ('quiz', 'ban', 'reportCount', 'clicks', 'reporters')