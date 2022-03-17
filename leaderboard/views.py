from django.shortcuts import render
from core.models import Streak, Profile
# Create your views here.


"""
Template wireframe

streak | question | and others
1(AI prediction) | 0 (Current one) | -1 (last week)
little explanation and link to full details

And then, the all the objects. 
"""

def StreakLeaderBoard(request):
    leaders = Streak.objects.all()[0:1000] or Streak.objects.all()
    # add the get absolute url function to the profile
    # add pagination and waypoint or ajax I think Ajax will be more controllable

    context = {
        'leaders': leaders,
    }

    return render(request, 'leaderboard/streak.html', context)


# add the function for reward that will be triggered by celery. it wont't be a view function

def WealthLeaderBoard(request,*args, **kwargs):
    leaders = Profile.objects.all().order_by('coins')[0:1000] or Profile.objects.all().order_by('coins')
    context = {
        'leaders' : leaders,
    }

    return render(request, 'leaderboard/wealth.html', context)