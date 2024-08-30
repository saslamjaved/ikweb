from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Course
from chapters.models import Chapter
from .forms import CourseForm, SearchForm

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'dashboard/home.html', {'courses': courses})

def course_detail(request, slug):
    course = get_object_or_404(Course, slug=slug) 
    chapters = Chapter.objects.filter(course=course)
    return render(request, 'courses/course_detail.html', {'course': course, 'chapters':chapters})
    #
    #return render(request, 'courses/course_detail.html', {'course': course,'chapters':chapters})

@login_required
def course_create(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('courses:course_list')
    else:
        form = CourseForm()
    return render(request, 'courses/course_form.html', {'form': form})

@login_required
def course_edit(request, slug):
    course = get_object_or_404(Course, slug=slug)
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()
            return redirect('courses:course_detail', slug=course.slug)
    else:
        form = CourseForm(instance=course)
    return render(request, 'courses/course_form.html', {'form': form})

def search_courses(request):
    form = SearchForm(request.GET or None)
    courses = Course.objects.all()
    #courses = Course.objects.none()  # Default to no results
    
    if form.is_valid():
        query = form.cleaned_data.get('query')
        print("Query", query)
        if query:
            courses = Course.objects.filter(title__icontains=query)
    return render(request, 'courses/search_results.html', {'form': form, 'courses': courses})            