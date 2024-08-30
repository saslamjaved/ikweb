from django.urls import path, include
from . import views

urlpatterns = [
    path('payments_detail/', views.payment_detail, name='payment_detail'),
    path('payments_init/', views.payments_init, name='payments_init'),
    path('payments_list/', views.payment_list, name='payment_list'),
   
]
