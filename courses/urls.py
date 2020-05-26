from django.urls import path

from . import views

urlpatterns = [
    path('courses', views.courses, name="courses"),
    path('<int:course_id>', views.course, name='course'),
    path('filter', views.filter, name="filter"),
]
