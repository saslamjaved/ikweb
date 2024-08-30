from django.db import models
from autoslug import AutoSlugField

class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title', unique=True)
    content = models.TextField()
    published_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
