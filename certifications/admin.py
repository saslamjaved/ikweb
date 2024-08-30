from django.contrib import admin
from .models import Certification

@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'date_issued')
    search_fields = ('user__username', 'course__title')
