from django.db import models
from django.contrib.auth.models import User


from quiz.models import Quizzes
from diary.models import Diary
from todo.models import Task

from datetime import date

from .utils import generate_ref_code
# from quiz.idpk import finalConvert

# Create your models here.
class Profile(models.Model):
    SEX =(
        ('male', 'male'),
        ('female', 'female'),
    )
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    middle_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    bio = models.TextField(max_length=1000, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=SEX, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    state_of_residence = models.CharField(max_length=100, null=True, blank=True)
    state_of_origin = models.CharField(max_length=100, null=True, blank=True)
    nationality = models.CharField(max_length=100, null=True, blank=True)
    picture = models.ImageField(null=True, blank=True)
    # quizAttempted = models.ManyToManyField(Quizzes, related_name="quiz_attempted")
    # quizCreated = models.ManyToManyField(Quizzes, related_name="quiz_created")
    date_joined = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, blank=True, null=True)
    streak = models.IntegerField(default=0, null=True, blank=True)
    # diaries = models.ManyToManyField(Diary)
    # tasks = models.ManyToManyField(Task)
    coins = models.IntegerField(default=0, null=True, blank=True)
    code = models.CharField(max_length=20, null=True, blank=True)
    referrer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="referrer")


    def get_referrer_profiles(self):
        pass


    def save(self, *args, **kwargs):
        if self.code == None:
            code = generate_ref_code()
            self.code = code
        super().save(*args, **kwargs)


    # @property
    # def get_number_of_quiz_created(self):
    #     return self.quizCreated.count()


    # @property
    # def get_number_of_quiz_attempted(self):
    #     return self.quizAttempted.count()


    # @property
    # def get_number_of_tasks(self):
    #     return self.tasks.count()
   
   
    # @property
    # def get_number_of_diaries(self):
    #     return self.diaries.count()
   

    @property
    def last_update(self):
        #use profile.last_update in the template
        # learn how to use the datetime and time functions in python
        days_length = date.today() - self.date_updated.date()
        days_length_shrink = str(days_length).split(',', 1)[0]
        return days_length_shrink


    @property
    def when_joined(self):
        days_length = date.today() - self.date_joined.date()
        days_length_shrink = str(days_length).split(',', 1)[0]
        return days_length_shrink


    # @property
    # def get_number_tasks(self):
    #     return self.tasks.count()


    # @property
    # def get_number_diaries(self):
    #     return self.diaries.count()


    def __str__(self):
        return f"{self.user.username}"

