from django.contrib import admin
from .models import Quiz, FourChoicesQuestion, TrueOrFalseQuestion, Category, Attempter, Attempt

# Register your models here.
admin.site.register(Quiz)
admin.site.register(FourChoicesQuestion)
admin.site.register(TrueOrFalseQuestion)
admin.site.register(Category)
admin.site.register(Attempter)
admin.site.register(Attempt)