from django.contrib import admin
from .models import CustomUser

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import UserRegistrationForm # Ensure you have a form for creating users

"""
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = UserRegistrationForm
    form = UserRegistrationForm
    list_display = ('email', 'user_type', 'phone_number', 'address', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'user_type')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'phone_number', 'address', 'user_type')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'phone_number', 'address', 'user_type', 'password1', 'password2'),
        }),
    )
    search_fields = ('username', 'email')
    ordering = ('username',)

admin.site.register(CustomUser, CustomUserAdmin)

"""
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'user_type', 'phone_number', 'address','street_address','city','state','postal_code','country')
    search_fields = ('username', 'email')
    list_filter = ('user_type',)
