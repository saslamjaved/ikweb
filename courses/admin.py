from django.contrib import admin
from .models import Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'thumbnail', 'subscription','slug')
    search_fields = ('title',)

