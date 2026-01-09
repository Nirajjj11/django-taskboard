from django.shortcuts import render

def main(request):
    data = {
        'title': "HomePage",
        'bdata': "Hello niraj",
        'tasks': [
            {"title": "Learn Django", "is_completed": False},
            {"title": "Build Taskboard", "is_completed": True},
        ]
    }
    return render(request, 'index.html', data)