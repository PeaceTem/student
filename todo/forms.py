from django import forms
#from ckeditor.widgets import CKeditorWidget
from .models import Task

class NewTaskForm(forms.ModelForm):
    
    class Meta:
        model = Task
        fields = ['title', 'description', 'complete']