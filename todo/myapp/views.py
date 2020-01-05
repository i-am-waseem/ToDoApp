import requests

from django.shortcuts import render, reverse
from django.utils import timezone
from django.http import HttpResponseRedirect
from .models import TodoTask

# Create your views here.
# def home(request):
#     return render(request, 'myapp/base.html')

def home(request):
    todo_list = TodoTask.objects.all().order_by('-task_created')
    return render(request, 'myapp/new_task.html',{'todo_list':todo_list})

def new_task(request):
    new_task = request.POST.get('add_task')
    if new_task:
        task = TodoTask(todo_task=new_task, task_created=timezone.now())
        task.save()
    return HttpResponseRedirect(reverse('home'))


def del_task(request, task_id):
    todo_list = TodoTask.objects.get(id=task_id).delete()
    return HttpResponseRedirect(reverse(home),{'todo_list':todo_list})
