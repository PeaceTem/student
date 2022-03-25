


from django.db import models
from django.contrib.auth.models import User


from quiz.models import Quiz, Category
from diary.models import Diary
from todo.models import Task
from question.models import QTrueOrFalseQuestion, QFourChoicesQuestion
from datetime import date, datetime, time

from .utils import generate_ref_code
# from quiz.idpk import finalConvert
from django.utils.text import slugify
from django.utils import timezone
import pytz


# Create your models here.


class Profile(models.Model):
    SEX =(
        ('male', 'male'),
        ('female', 'female'),
    )
    user = models.OneToOneField(User,null=True, blank=True, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='images/', null=True, blank=True)
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
    slug = models.SlugField(default='')
    coins = models.DecimalField(default=100.0, decimal_places=2, max_digits=200)
    date_updated = models.DateTimeField(auto_now=True)
    code = models.CharField(max_length=32, null=True, blank=True)
    refercount = models.PositiveIntegerField(default=0)
    views = models.PositiveIntegerField(default=0)
    categories = models.ManyToManyField(Category, blank=True, related_name='profileCategories')
    quizTaken = models.ManyToManyField(Quiz, blank=True, related_name='profileQuizTaken')
    trueOrFalseQuestionsMissed = models.ManyToManyField(QTrueOrFalseQuestion, blank=True, related_name='trueOrFalseQuestionsMissed')
    fourChoicesQuestionsMissed = models.ManyToManyField(QFourChoicesQuestion, blank=True, related_name='fourChoicesQuestionsMissed')
    quizAvgScore = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    questionAvgScore = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    quizAttempts = models.IntegerField(default=0)
    questionAttempts = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    quizzes = models.IntegerField(default=0)

    




    class Meta:
        ordering = ['-coins']


    def get_recommended_profiles(self):
        # qs = Profile.objects.all()
        # my_recs = [p for p in qs if p.recommended_by == self.user]
        my_recs = Profile.objects.filter(referrer=self.user)
        return my_recs


    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.user.username)
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
   

    # @property
    # def last_update(self):
    #     #use profile.last_update in the template
    #     # learn how to use the datetime and time functions in python
    #     days_length = date.today() - self.date_updated.date()
    #     days_length_shrink = str(days_length).split(',', 1)[0]
    #     return days_length_shrink


    # @property
    # def when_joined(self):
    #     days_length = date.today() - self.date_joined.date()
    #     days_length_shrink = str(days_length).split(',', 1)[0]
    #     return days_length_shrink


    def __str__(self):
        return f"{self.user}"


 
class Follower(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    followers = models.ManyToManyField(User, blank=True, related_name='followers') 
    following = models.ManyToManyField(User, blank=True, related_name='following')

    def __str__(self):
        return f"{self.id}"
# create the streak in the app views and validate it thereafter
class Streak(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, null=True, blank=True)
    active = models.BooleanField(default=False)
    usedDate = models.DateField(auto_now=True, null=True, blank=True)
    length = models.PositiveIntegerField(default=0)
    question = models.PositiveIntegerField(default=0)
    freeze = models.BooleanField(default=False)

    class Meta:
        ordering = ['-length', '-question', '-freeze', '-id']


    def __str__(self):
        return f"{self.profile.user.username} | {self.length} | {str(self.active)}"

# alert users whenever they earn a streak

    def validateStreak(self, *args, **kwargs):

        duration = date.today() - self.usedDate
        print('first duration', duration)
        durationHours = duration.seconds//3600
        print('Hours', durationHours)
        duration = duration.days
        print('duration', duration)
        if duration == 0:

            self.question += 1

            if self.question == 20 and self.active == False:
                self.length += 1
                self.active = True
                self.profile.coins += 10
                self.profile.save()

            elif self.question == 50 and self.active == True:
                self.profile.coins += 10
                self.profile.save()
            
            elif self.question == 100 and self.active == True:
                self.profile.coins += 30
                self.profile.save()
                
            super().save(*args, **kwargs)

        # add streak freeze product in the wallet
        # users can pay us dollars to buy anything
        elif duration == 1:
            self.question = 0
            self.active = False

            super().save(*args, **kwargs)

        elif duration > 1:
            self.question = 0
            self.active = False

            if self.freeze:
                self.freeze = False
            else:
                self.length = 0

            super().save(*args, **kwargs)


        # return self.length


    def save(self, *args, **kwargs):
        # self.date = datetime.combine(datetime.now.(), datetime.min.time(), tzinfo=pytz.UTC)
        self.usedDate = date.today()
        print('local date demo', self.usedDate)
        super().save(*args, **kwargs)

    

    class Meta:
        ordering = ['-length', '-question']






class Link(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, blank=True)
    url = models.URLField(null=True, blank=True)


    def __str__(self):
        return f"{self.profile}"




