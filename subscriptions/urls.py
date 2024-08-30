from django.urls import path, include
from . import views

urlpatterns = [
    path('subscription_list/', views.subscription_list, name='subscription_list'),
#    path('', include('payments.urls')), 
]
