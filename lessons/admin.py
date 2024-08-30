from django.contrib import admin
from .models import Lesson

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('course','chapter','title', 'video_link','duration','content','slug')
    search_fields = ('title', 'course__title','chapter__title')