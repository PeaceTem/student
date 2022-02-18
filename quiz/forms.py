from django import forms
# from ckeditor.widgets import CKeditorWidget
from .models import Quizzes, Question, Answer, Category

class NewQuizForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(), required=True)
    public = forms.BooleanField()

    class Meta:
        model = Quizzes
        fields = ('title', 'description','public',)

class NewQuestionForm(forms.ModelForm):
    # question_text = forms.
    class Meta:
        model = Question
        fields = ('question_text', 'points')

class NewAnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('answer_text', 'is_correct')
        

class NewCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('title',)