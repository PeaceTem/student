from django import forms
#from ckeditor.widgets import CKeditorWidget
from .models import Diary

class NewDiaryForm(forms.ModelForm):
    
    class Meta:
        model = Diary
        fields = ['title', 'post',]

    