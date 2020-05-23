from django.urls import path

from . import views

urlpatterns = [
    path('allcourses', views.index, name="allcourse"),
    path('<int:course_id', views.course, name="course"),
    path('filter', views.filter, name="filter"),
]
