from django.urls import path

from . import views

urlpatterns = [
    path('courses', views.courses, name="courses"),
    path('<int:course_id>', views.course, name='course'),
    path('pastry', views.pastry, name="pastry"),
    path('cakes', views.cakes, name="cakes"),
    path('breads', views.breads, name="breads"),
]
