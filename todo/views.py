from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Task
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .forms import NewTaskForm
# Create your views here.

class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url= reverse_lazy('todo:tasks')



# Create your views here.

@login_required(login_url='login')
def TaskList(request):
    tasks = Task.objects.filter(user=request.user)
    count = tasks.count()

    search_input= request.GET.get('search-area') or ''
    if search_input:
        tasks = Task.objects.filter(title__icontains=search_input)


    context={
        'tasks': tasks,
        'count': count,
    }

    return render(request, 'todo/task_list.html', context)



@login_required(login_url='login')
def TaskDetail(request, pk):
    task= get_object_or_404(Task, id=pk)
    context={
        'task': task,
    }
    return render(request, 'todo/task_detail.html', context)

@login_required(login_url='login')
def TaskCreate(request):
    user = request.user
    form = NewTaskForm()

    if request.method == 'POST':
        form = NewTaskForm(request.POST)
        if form.is_valid():
            title= form.cleaned_data.get('title')
            description = form.cleaned_data.get('description')
            complete = form.cleaned_data.get('complete')
            Task.objects.create(user=user, title=title, description=description, complete=complete)
            return redirect('todo:tasks')
        
    context={
        'form': form,
    }

    return render(request, 'todo/task_form.html', context)



@login_required(login_url='login')
def TaskUpdate(request, pk):
    task=get_object_or_404(Task, id=pk)
    if request.user != task.user:
        return HttpResponseForbidden
    
    form = NewTaskForm(instance=task)
    if request.method == 'POST':
        form = NewTaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('todo:tasks')

    context={
        'form': form,
        'task': task,
    }
    return render(request, 'todo/task_update.html', context)



# create the quiz delete view
@login_required(login_url='login')
def DeleteTask(request, pk):
    task = get_object_or_404(Task, id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('todo:tasks')
    
    return render(request, 'todo/task_confirm_delete.html', {'task': task})
