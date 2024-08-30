from django.contrib import admin
from .models import Chapter

@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'video_link')
    search_fields = ('title', 'course__title')
