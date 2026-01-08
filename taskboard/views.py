from django.shortcuts import render

def main(request):
    data = {
        'title': "HomePage",
        'bdata': "Hello niraj",
    }
    return render(request, 'index.html', data)