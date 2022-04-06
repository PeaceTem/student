from django.shortcuts import render, redirect
from django.http import HttpResponse

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




def PostAdClick(request, post_id):
    # link_id = request.GET.get('link_id')

    postAd = PostAd.objects.get(id=post_id)

    postAd.clicks += 1
    postAd.save()
    print(postAd.clicks)

    return HttpResponse('clicked')