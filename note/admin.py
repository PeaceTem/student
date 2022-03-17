from django.contrib import admin
from .models import Note
# Register your models here.

admin.site.register(Note)


# user should be able to upload image to their diary
# their should be teacher mode and students mode for courses that will be created
# their should be passcode for other user to check one's note
