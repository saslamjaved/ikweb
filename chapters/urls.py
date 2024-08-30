from django.urls import path, include
from . import views

urlpatterns = [
    #path('<slug:slug>', views.chapter_details, name='chapter_details'),
    path('<slug:slug>/', views.chapter_details, name='chapter_details'),
    path('chapter_list/<int:pk>/', views.chapter_list, name='chapter_list'),  
]
