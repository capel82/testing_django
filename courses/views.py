from django.shortcuts import render
# Create your views here.
def index(request):
    return render(request, 'pages/allcourses.html')

def pastry(request):
    return render(request,'pages/pastry.html')

def cakes(request):
    return render(request,'pages/cakes.html')

def breads(request):
    return render(request,'pages/breads.html')

def filter(request):
    return render(request,'pages/filter.html')