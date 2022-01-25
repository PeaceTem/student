from django.shortcuts import render, redirect
from .models import Diary
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login

# Create your views here.

class DiaryList(ListView):
    model = Diary
    #paginate_by = 2
    context_object_name = 'diaries'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['diaries'] = context['diaries'].filter(user=self.request.user)
        context['count'] = context['diaries'].filter(user=self.request.user).count()
        
        return context
        

class DiaryDetail(DetailView):
    model = Diary
    context_object_name = 'diary'


class DiaryCreate(CreateView):
    model = Diary
    fields = '__all__'
    success_url = reverse_lazy('diaries')


class DiaryUpdate(UpdateView):
    model = Diary
    fields = '__all__'
    success_url = reverse_lazy('diaries')