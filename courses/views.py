from django.shortcuts import render
from .models import Course
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

#courses displayed by date of weekday and filter to only courses that are published.
def courses(request):
    courses = Course.objects.order_by('weekday_datetime').filter(is_published=True)
    #pagination for all course
    paginator = Paginator (courses, 6)
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