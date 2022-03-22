from django.shortcuts import render, redirect

from .models import PostAd
from .forms import NewPostAdForm
from random import shuffle
from quiz.utils import randomChoice
# Create your views here.

def PostAdView(request):
    postAd = PostAd.objects.all()
    postAd = randomChoice(postAd)
    print(postAd)
    # change the shuffle to random
    

    context={
        'postAd': postAd,
    }

    return render(request, 'ads/postAd.html', context)