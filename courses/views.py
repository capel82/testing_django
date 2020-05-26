from django.shortcuts import render
from .models import Course

# Create your views here.
def index(request):
    courses = Course.objects.all()

    content = {
        'courses' : courses
    }
    return render(request, 'pages/allcourses.html', content)

def pastry(request):
    return render(request,'pages/pastry.html')

def cakes(request):
    return render(request,'pages/cakes.html')

def breads(request):
    return render(request,'pages/breads.html')

def filter(request):
    return render(request,'pages/filter.html')