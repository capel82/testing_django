from django.shortcuts import render
from .models import Course
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


def courses(request):
    courses = Course.objects.all()
    #pagination for all course
    paginator = Paginator (courses, 3)
    page = request.GET.get('page')

    paged_courses = paginator.get_page(page)

    content = {
        'courses' : paged_courses
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