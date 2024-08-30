from django import forms
from .models import Chapter

class ChapterForm(forms.Form):
    class Meta:
        model = Chapter        
        fields = ['title','video_link', 'content','slug']