from django.db import models
from autoslug import AutoSlugField

class Chapter(models.Model):
    course = models.ForeignKey('courses.Course', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title', unique=True)
    video_link = models.URLField()
    content = models.TextField()
    duration = models.PositiveIntegerField(default=10)
    order = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.title} - {self.course.title}'
