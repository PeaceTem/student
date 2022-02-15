from django.shortcuts import render, redirect, get_object_or_404
from .models import Diary
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login


from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .forms import NewDiaryForm

from django.core.mail import send_mail


def contact(request):
    if request.method == 'POST':
        message_name = request.POST.get('message_name')
        message_email = request.POST.get('message_email')
        message = request.POST.get('message')

        # send an email
        send_mail(
            message_name, #the subject
            message, # message
            message_email, # the sender
            ['oakande458@stu.ui.edu.ng'] # receiver,
        )

        return render(request, 'diary/contact.html', {'message_name': message_name})

    else:
        return render(request, 'diary/contact.html', {})



# Create your views here.
@login_required(login_url='login')
def DiaryList(request):
    diaries = Diary.objects.filter(user=request.user)
    count = diaries.count()

    context={
        'diaries': diaries,
        'count': count,
    }

    return render(request, 'diary/diary_list.html', context)



@login_required(login_url='login')
def DiaryDetail(request, pk):
    diary= get_object_or_404(Diary, id=pk)
    context={
        'diary': diary,
    }
    return render(request, 'diary/diary_detail.html', context)

@login_required(login_url='login')
def DiaryCreate(request):
    user = request.user
    form = NewDiaryForm()

    if request.method == 'POST':
        form = NewDiaryForm(request.POST)
        if form.is_valid():
            title= form.cleaned_data.get('title')
            post=form.cleaned_data.get('post')
            Diary.objects.create(user=user, title=title, post=post)
            return redirect('diary:diaries')
        
    context={
        'form': form,
    }

    return render(request, 'diary/diary_form.html', context)



@login_required(login_url='login')
def DiaryUpdate(request, pk):
    diary=get_object_or_404(Diary, id=pk)
    if request.user != diary.user:
        return HttpResponseForbidden
    
    form = NewDiaryForm(instance=diary)
    if request.method == 'POST':
        form = NewDiaryForm(request.POST, instance=diary)
        if form.is_valid():
            form.save()
            return redirect('diary:diaries')

    context={
        'form': form,
        'diary': diary,
    }
    return render(request, 'diary/diary_update.html', context)


