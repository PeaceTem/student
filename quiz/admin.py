from django.contrib import admin
from .models import Quiz, FourChoicesQuestion, TrueOrFalseQuestion, Category

# Register your models here.
admin.site.register(Quiz)
admin.site.register(FourChoicesQuestion)
admin.site.register(TrueOrFalseQuestion)
admin.site.register(Category)