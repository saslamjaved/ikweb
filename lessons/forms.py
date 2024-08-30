from django import forms
from .models import Lesson

class LessonForm(forms.Form):
    class Meta:
        model = Lesson        
        fields = ['course','chapter','title', 'video_link','duration','content','slug']