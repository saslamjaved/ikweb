from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import Payment

User = get_user_model()

@login_required
def payment_list(request):
    payments = Payment.objects.filter(user=request.user)
    return render(request, 'payments/payment_list.html', {'payments': payments})

@login_required
def payment_detail(request, id):
    payment = get_object_or_404(Payment, id=id, user=request.user)
    return render(request, 'payments/payment_detail.html', {'payment': payment})

def payments_init(request):
    user_details = get_object_or_404(User,username=request.user,)
    user1=User.objects.filter(username=request.user)
    print("(((((((())))))))")
    print(user1)
    print("(((((((())))))))")
    if not request.user.is_authenticated:
        return redirect("register")
    #payment = get_object_or_404(Payment,user=request.user)
    return render(request, 'payments/payments_init.html',{"user_details":user_details})    
