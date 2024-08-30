from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Subscription

@login_required
def subscription_list(request):
    subscriptions = Subscription.objects.all()
    user_enroll_details = Enrollment.objects.filter(user=user).values()
    return render(request, 'subscriptions/subscription_list.html', {'subscriptions': subscriptions,"user_enroll_details":user_enroll_details})

@login_required
def subscribe(request, subscription_id):
    subscription = get_object_or_404(Subscription, id=subscription_id)
    user = request.user
    # Implement subscription logic (e.g., saving to user's subscriptions)
    # For demonstration, we will just redirect to subscription list
    return redirect('subscriptions:subscription_list')
