from django.shortcuts import render
from .models import Course

# Create your views here.
def courses(request):
    courses = Course.objects.all()

    content = {
        'courses' : courses
    }
    return render(request, 'pages/courses.html', content)

def course(request, course_id):
    return render(request,'pages/course.html')

def cakes(request):
    return render(request,'pages/cakes.html')

def breads(request):
    return render(request,'pages/breads.html')

def filter(request):
    return render(request,'pages/filter.html')