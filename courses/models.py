from django.db import models
from autoslug import AutoSlugField

class Course(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title', unique=True)
    description = models.TextField()
    video_link = models.URLField()
    thumbnail = models.ImageField(upload_to='thumbnails/')
    subscription = models.ForeignKey('subscriptions.Subscription', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title
