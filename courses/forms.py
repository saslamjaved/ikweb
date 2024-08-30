from django import forms
from .models import Course

class CourseForm(forms.Form):
    class Meta:
        model = Course        
        fields = ['title','description', 'video_link', 'thumbnail', 'subscription','slug']

class SearchForm(forms.Form):
    query = forms.CharField(label='Search Courses', max_length=100, required=False)