from django.contrib import admin

from .models import Course
# models for admin table so the id and title are linked, filter category, editable options and ordering datetime.
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category','weekday_datetime','weekends_datetime', 'is_published', 'is_next_event')
    list_display_links = ('id', 'title')
    list_filter = ('category',)
    list_editable = ('is_published', 'is_next_event')
    list_per_page = 20
    ordering = ('weekday_datetime',)

admin.site.register(Course, CourseAdmin)