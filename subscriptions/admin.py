from django.contrib import admin
from .models import Subscription, Enrollment

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'duration')
    search_fields = ('name',)

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'subscription', 'enrolled_at','end_date','status')
    search_fields = ('subsciption',)