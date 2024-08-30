from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth import get_user_model

class Subscription(models.Model):
    name = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='name', unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.CharField(max_length=20)  # e.g., 'Monthly', 'Yearly'

    def __str__(self):
        return self.name

class Enrollment(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('expired', 'Expired'),
    ]    
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)
    enrolled_at = models.DateTimeField(auto_now_add=True)
    end_date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='inactive')

    # You can add more fields like subscription expiration, status, etc.

    class Meta:
        unique_together = ('user', 'subscription')

    def is_active(self):
        today = date.today()
        return self.start_date <= today <= self.end_date and self.status == 'active'
        