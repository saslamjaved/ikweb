from django.urls import path, include
from . import views

urlpatterns = [
    path('blog_detail/', views.blog_detail, name='blog_detail'),
    path('blog_list/', views.blog_list, name='blog_list'),
]
