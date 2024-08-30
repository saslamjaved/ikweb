from django.db import models
from courses.models import Course
from chapters.models import Chapter
from autoslug import AutoSlugField

class Lesson(models.Model):
    course = models.ForeignKey('courses.Course', on_delete=models.CASCADE)
    chapter = models.ForeignKey('chapters.Chapter', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title', unique=True)
    video_link = models.URLField()
    duration = models.FloatField(blank=True)
    content = models.TextField()

    def __str__(self):
        return f'{self.title} - {self.chapter.title}'
