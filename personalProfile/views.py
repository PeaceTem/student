from django.shortcuts import render, get_object_or_404, redirect
from core.models import Profile, Follower, Link
from django.contrib.auth.models import User
from quiz.models import Quiz
from question.models import QTrueOrFalseQuestion, QFourChoicesQuestion
# Create your views here.


def MassProfile(request, profile_name):
    try:
        user = User.objects.get(username=profile_name) or None
        profile = get_object_or_404(Profile, user=user)
        follower = get_object_or_404(Follower, user=user)
        link = Link.objects.get(profile=profile)
        if user != request.user:
            profile.views += 1
            profile.save()
        
    except:
        return redirect('quiz:quizzes')
    
    context = {
        'profile': profile,
        'follower' : follower,
        'link': link,
        'nav': 'profile',
    }

    return render(request, 'core/profile.html', context)
