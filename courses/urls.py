from django.urls import path

from . import views

urlpatterns = [
    path('allcourses', views.index, name="allcourse"),
    path('pastry', views.pastry, name="pastry"),
    path('cakes', views.cakes, name="cakes"),
    path('breads', views.breads, name="breads"),
    path('filter', views.filter, name="filter"),
]
