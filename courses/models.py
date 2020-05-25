from django.db import models
from datetime import datetime

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length =50)
    learn_list1 = models.CharField(max_length=250)
    learn_list2 = models.CharField(max_length=250)
    learn_list3 = models.CharField(max_length=250, blank=True)
    completion_list1 = models.CharField(max_length=250)
    completion_list2 = models.CharField(max_length=250, blank=True)
    category = models.CharField(max_length=50)
    weekday_datetime = models.DateField()
    weekends_datetime = models.DateField()
    photo_course = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_next_event = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)
    price = models.IntegerField()

def _str_(self):
    return self.title
    