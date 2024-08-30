from django.contrib.auth.models import AbstractUser
from django.db import models
from autoslug import AutoSlugField
from django_countries.fields import CountryField

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    country = models.CharField(max_length=100,default="IN")
    state = models.CharField(max_length=100, blank=True, null=True, default="TS")
    city = models.CharField(max_length=100,default="Hyderabad")
    postal_code = models.CharField(max_length=20,default="50030")
    street_address = models.CharField(max_length=255,default="Rajendranagar")
    slug = AutoSlugField(populate_from='username', unique=True)

    USER_GROUPS = (
        ('admin', 'Admin'),
        ('mentor', 'Mentor'),
        ('consumer', 'Consumer'),
    )
    user_type = models.CharField(max_length=20, choices=USER_GROUPS, default='consumer')

    def __str__(self):
        return self.username if self.username else "Unknown User"
