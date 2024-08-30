from django.db import models
from django.contrib.auth import get_user_model

class Certification(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    course = models.ForeignKey('courses.Course', on_delete=models.CASCADE)
    date_issued = models.DateField(auto_now_add=True)
    certificate_code = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f'Certificate for {self.user.username} - {self.course.title}'
