from django.contrib import admin
from .models import Answer, Question, Quizzes, Attempter, Attempt, Profile
# Register your models here.
admin.site.register(Answer)
admin.site.register(Question)
admin.site.register(Quizzes)
admin.site.register(Attempter)
admin.site.register(Attempt)
admin.site.register(Profile)
