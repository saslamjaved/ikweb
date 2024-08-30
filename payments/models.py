from django.db import models
from django.contrib.auth import get_user_model

class Payment(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[('success', 'Success'), ('failed', 'Failed')])
    timestamp = models.DateTimeField(auto_now_add=True)
    receipt = models.FileField(upload_to='receipts/')

    def __str__(self):
        return f'Payment {self.id} - {self.status}'
