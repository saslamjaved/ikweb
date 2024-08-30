from django.urls import path, include
from . import views

urlpatterns = [
    path('certification_detail/', views.certification_detail, name='certification_detail'),
    path('certification_list/', views.certification_list, name='certification_list'),
]
