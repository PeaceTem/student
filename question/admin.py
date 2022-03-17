from django.contrib import admin
from .models import QTrueOrFalseQuestion, QFourChoicesQuestion
# Register your models here.


admin.site.register(QTrueOrFalseQuestion)
admin.site.register(QFourChoicesQuestion)
