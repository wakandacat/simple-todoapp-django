from django.shortcuts import render
from .models import Task
from .forms import TaskForm
from django.shortcuts import redirect
from user_agents import parse


def index(request):
    tasks = Task.objects.all()
    form = TaskForm()

    return render(request, 'index.html', {'tasks': tasks, 'form': form})


def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()

    return redirect('index')


def delete_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.delete()
    return redirect('index')