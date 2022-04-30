


from django.db import models
from django.contrib.auth.models import User


from quiz.models import Quiz
from category.models import Category
from question.models import TrueOrFalseQuestion, FourChoicesQuestion
from datetime import date, datetime, time, timedelta

from .utils import generate_ref_code
# from quiz.idpk import finalConvert
from django.utils.text import slugify
from django.utils import timezone
import pytz


from .managers import ProfileManager

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
    coins = models.DecimalField(default=20.0, decimal_places=2, max_digits=200)
    date_updated = models.DateTimeField(auto_now=True)
    code = models.CharField(max_length=32, null=True, blank=True)
    refercount = models.PositiveIntegerField(default=0)
    views = models.PositiveIntegerField(default=0)
    categories = models.ManyToManyField(Category, blank=True, related_name='profileCategories')
    quizTaken = models.ManyToManyField(Quiz, blank=True, related_name='profileQuizTaken')
    trueOrFalseQuestionsTaken = models.ManyToManyField(TrueOrFalseQuestion, blank=True, related_name='trueOrFalseQuestionsTaken')
    fourChoicesQuestionsTaken = models.ManyToManyField(FourChoicesQuestion, blank=True, related_name='fourChoicesQuestionsTaken')
    
    trueOrFalseQuestionsMissed = models.ManyToManyField(TrueOrFalseQuestion, blank=True, related_name='trueOrFalseQuestionsMissed')
    fourChoicesQuestionsMissed = models.ManyToManyField(FourChoicesQuestion, blank=True, related_name='fourChoicesQuestionsMissed')
    quizAvgScore = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    questionAvgScore = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    quizAttempts = models.IntegerField(default=0)
    questionAttempts = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    quizzes = models.IntegerField(default=0)
    favoriteQuizzes = models.ManyToManyField(Quiz, blank=True, related_name='favoriteQuizzes')
    



    objects = ProfileManager()


    

    @property
    def get_number_of_quiz_created(self):
        num = self.quizzes
        if num < 1000:
            return num
        elif num < 1000000:
            num = num / 1000
            num = round(num, 1)
            return f"{num}k"
        elif num < 1000000000:
            num = num / 1000000
            num = round(num, 1)
            return f"{num}M"
        elif num < 1000000000000:
            num = num / 1000000000
            num = round(num, 1)
            return f"{num}B"
        return num






    @property
    def get_number_of_likes(self):
        num = self.likes
        if num < 1000:
            return num
        elif num < 1000000:
            num = num / 1000
            num = round(num, 1)
            return f"{num}k"
        elif num < 1000000000:
            num = num / 1000000
            num = round(num, 1)
            return f"{num}M"
        elif num < 1000000000000:
            num = num / 1000000000
            num = round(num, 1)
            return f"{num}B"
        return num


    @property
    def get_number_of_quizzes_attempted(self):
        num = self.quizAttempts
        if num < 1000:
            return num
        elif num < 1000000:
            num = num / 1000
            num = round(num, 1)
            return f"{num}k"
        elif num < 1000000000:
            num = num / 1000000
            num = round(num, 1)
            return f"{num}M"
        elif num < 1000000000000:
            num = num / 1000000000
            num = round(num, 1)
            return f"{num}B"
        return num




    @property
    def get_number_of_questions_attempted(self):
        num = self.questionAttempts
        if num < 1000:
            return num
        elif num < 1000000:
            num = num / 1000
            num = round(num, 1)
            return f"{num}k"
        elif num < 1000000000:
            num = num / 1000000
            num = round(num, 1)
            return f"{num}M"
        elif num < 1000000000000:
            num = num / 1000000000
            num = round(num, 1)
            return f"{num}B"
        return num


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


    @property
    def get_number_of_followers(self):
        num = self.followers
        if num < 1000:
            return num
        elif num < 1000000:
            num = num / 1000
            num = round(num, 1)
            return f"{num}k"
        elif num < 1000000000:
            num = num / 1000000
            num = round(num, 1)
            return f"{num}M"
        elif num < 1000000000000:
            num = num / 1000000000
            num = round(num, 1)
            return f"{num}B"
        return num



    @property
    def get_number_of_following(self):
        num = self.following
        if num < 1000:
            return num
        elif num < 1000000:
            num = num / 1000
            num = round(num, 1)
            return f"{num}k"
        elif num < 1000000000:
            num = num / 1000000
            num = round(num, 1)
            return f"{num}M"
        elif num < 1000000000000:
            num = num / 1000000000
            num = round(num, 1)
            return f"{num}B"
        return num

    def __str__(self):
        return f"{self.id}"
# create the streak in the app views and validate it thereafter


class Streak(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, null=True, blank=True)
    active = models.BooleanField(default=False)
    currentDate = models.DateField(auto_now=True, null=True, blank=True)
    
    length = models.PositiveIntegerField(default=0)
    question = models.PositiveIntegerField(default=0)
    freeze = models.BooleanField(default=False)

    class Meta:
        ordering = ['-length', '-question', '-freeze', '-id']


    def __str__(self):
        return f"{self.profile.user.username} | {self.length} | {str(self.active)}"

# alert users whenever they earn a streak

    def validateStreak(self, *args, **kwargs):
        print(self.currentDate)
        duration = date.today() - self.currentDate
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
                self.profile.coins += 20
                self.profile.save()

            elif self.question == 50 and self.active == True:
                self.profile.coins += 60
                self.profile.save()
            
            elif self.question == 100 and self.active == True:
                self.profile.coins += 120
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
        self.currentDate = date.today()
        print('local date demo', self.currentDate)
        super().save(*args, **kwargs)

    

    class Meta:
        ordering = ['-length', '-question']





# add description
class Link(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    description = models.TextField(max_length=200,blank=True, null=True)
    clicks = models.PositiveIntegerField(default=0)
    date_updated = models.DateTimeField()




    @property
    def get_number_of_clicks(self):
        num = self.clicks
        if num < 1000:
            return num
        elif num < 1000000:
            num = num / 1000
            num = round(num, 1)
            return f"{num}k"
        elif num < 1000000000:
            num = num / 1000000
            num = round(num, 1)
            return f"{num}M"
        elif num < 1000000000000:
            num = num / 1000000000
            num = round(num, 1)
            return f"{num}B"
        return num

    def save(self, *args, **kwargs):
        if timezone.now() - date_updated < timedelta(days=30):
            messages.error(self.request, 'This link can only be changed every 30 days!')
            return None
        return super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.profile}"




