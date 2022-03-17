# from django import forms

# from .models import DraftQuiz, DraftFourChoicesQuestion, DraftTrueOrFalseQuestion

# class NewDraftQuizForm(forms.ModelForm):

#     class Meta:
#         model = DraftQuiz
#         fields = '__all__'
#         exclude = ('user','date', 'date_updated', 'categories', 'fourChoicesQuestions', 'trueOrFalseQuestions', 'lastQuestionIndex', 'questionLength', 'totalScore', 'attempts','gross_average_score','average_score', 'public',)
      


# class NewDraftFourChoicesQuestionForm(forms.ModelForm):

#     class Meta:
#         model = DraftFourChoicesQuestion
#         fields = '__all__'
#         exclude = ('user',  'index', 'form')



# class NewDraftTrueOrFalseQuestionForm(forms.ModelForm):

#     class Meta:
#         model = DraftTrueOrFalseQuestion
#         fields = '__all__'
#         exclude = ('user', 'index', 'form','answer1', 'answer2',)

