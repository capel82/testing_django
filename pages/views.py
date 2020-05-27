from django.shortcuts import render
from courses.models import Course
# Create your views here.

def index(request):
    #published course that is the next event
    courses = Course.objects.all().filter(is_published=True, is_next_event=True)

    content = {
        'courses' : courses
    }
    return render(request, 'pages/index.html', content)

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    return render(request,'pages/contact.html')

