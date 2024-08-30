from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.room_list, name='room_list'),
    path('room/<int:room_id>/', views.room_detail, name='room_detail'),
    
]
