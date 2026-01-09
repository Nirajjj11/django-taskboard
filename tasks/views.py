from django.shortcuts import render
from .models import Task
from django.http import JsonResponse

def home(request):
    data = {
        'all_tasks': Task.objects.all(),
        'title': "Task"
    }


    return render(request, "task.html", data)


def add_task(request):
    if request.method == "POST":
        task = Task.objects.create(
            title=request.POST.get("title"),
            description=request.POST.get("description")
        )
        return JsonResponse({"status": "saved", "id": task.id})

    return render(request, "entertask.html", {"title": "Task Entry"})
