from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from chapters.models import Chapter
from courses.models import Course
from subscriptions.models import Subscription, Enrollment
from lessons.models import Lesson
from chapters.forms import ChapterForm

def lessons_details(request, slug):
        print("slug is :",slug)
        lesson = get_object_or_404(Lesson, slug=slug)
        chapters = Chapter.objects.filter(course=lesson.course)
        print(lesson)
        print("$$$$$$")
        for i in chapters:
            print(i)

        context={
            'course':lesson.course,
            'chapter':lesson.chapter,
        }
        return render(request, 'lessons/lessons_details.html', {'lesson': lesson,'course':lesson.course,'chapter':lesson.chapter,'chapters':chapters})

@login_required
def lesson_list(request):
    lessons = Lesson.objects.all()
    return render(request, 'dashboard/home.html', {'lessons': lessons})
"""
@login_required
def lesson_detail(request, slug):
    chapter = get_object_or_404(Chapter, slug=slug)
    print("$$$$$$$^^^")
    print(chapter)
    print("$$$$$$$^^^")    
    chapters = Chapter.objects.filter(course=course)
    return render(request, 'courses/course_detail.html', {'course': course,'chapters':chapters})

def lessons_details(request, slug):
    #chapter = get_object_or_404(Chapter, slug=slug)
    lesson = get_object_or_404(Lesson, slug=slug)
    #subsciption = get_object_or_404(Subscription, slug=slug)
    course = lesson.course
    subscription = Subscription.objects.filter(course=course).values()
    enroll = Subscription.objects.filter(course=course)
    chapters = Chapter.objects.filter(course=course)
    chapter = Chapter.objects.filter(course=course)
    lessons = Lesson.objects.filter(chapter=chapter)
    subsc=subscription[0]['id']
    
    if chapter.order > 2:
        print("Inside")
        if not user_is_enrolled(request.user,subsc):
            return render(request, 'subscriptions/subscription_list.html')
    return render(request, 'lessons/lessons_details.html', {'lesson': lesson,'chapter':chapter,'chapters':chapters,'lessons':lessons})


def user_is_enrolled(user, subscription):
    print("Frm user_is_enrolled function")
    print(user,subscription)
    return Enrollment.objects.filter(user=user, subscription=subscription).exists()

"""