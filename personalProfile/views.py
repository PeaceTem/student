from django.shortcuts import render, get_object_or_404, redirect
from core.models import Profile, Follower
from django.contrib.auth.models import User
from quiz.models import Quiz
from question.models import QTrueOrFalseQuestion, QFourChoicesQuestion
# Create your views here.


def MassProfile(request, profile_name):
    try:
        user = User.objects.get(username=profile_name) or None
        profile = get_object_or_404(Profile, user=user)
        follower = get_object_or_404(Follower, user=user)
        quizzes = Quiz.objects.filter(user=profile.user)
        
    except:
        return redirect('quiz:quizzes')
    
    context = {
        'profile': profile,
        'follower' : follower,
        'quizzes': quizzes,
    }

    return render(request, 'core/profile.html', context)

#     visitor = request.user or None

# if not visitor:
#         code = str(kwargs.get('ref_code'))
#         print('This is the code', code)
#         try:
#             profile = get_object_or_404(Profile, code=code)
#             profile.coins += 50
#             profile.save()
#             print('This is the profile', profile)
#         except:
#             pass
