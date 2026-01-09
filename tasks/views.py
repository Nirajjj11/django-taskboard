from django.shortcuts import render
from .models import Task

def home(request):
    data = {
        'all_tasks': Task.objects.all(),
        'title': "Task"
    }


    return render(request, "task.html", data)
