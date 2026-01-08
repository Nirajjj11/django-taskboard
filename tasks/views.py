from django.shortcuts import render
from .models import Task

def home(request):
    all_tasks = Task.objects.all()
    return render(request, "HomePage.html", {"tasks": all_tasks})
