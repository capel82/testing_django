from django.shortcuts import render
# Create your views here.
def index(request):
    return render(request, 'pages/allcourses.html')

def course(request):
    return render(request,'pages/course.html')

def filter(request):
    return render(request,'pages/filter.html')