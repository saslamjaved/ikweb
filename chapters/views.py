from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import Chapter
from courses.models import Course
from subscriptions.models import Subscription, Enrollment
from lessons.models import Lesson
from .forms import ChapterForm

User = get_user_model()

def chapter_list(request,pk):
    course = get_object_or_404(Course, pk=pk)
    chapters = Chapter.objects.filter(course__id=pk)
    #chapters = Chapter.objects.all()
    return render(request, 'chapters/chapter_list.html', {'chapters': chapters})

def chapter_details(request, slug):
    chapter = get_object_or_404(Chapter, slug=slug)
    if request.user.is_authenticated:
        u1=request.user
    else:
        u1=4
    print("***************")
    print("User", u1)
    print("***************")
    if not Enrollment.objects.filter(user=u1).exists:
        usubsc=4
    else:
        user_enroll_details = Enrollment.objects.filter(user=u1).values()
        usubsc=user_enroll_details[0]['subscription_id']

    print("usubsc : ",usubsc)
    course = chapter.course
    subscription = Subscription.objects.filter(course=course).values()
    chapters = Chapter.objects.filter(course=course)
    lessons = Lesson.objects.filter(chapter=chapter)
    subsc=subscription[0]['id']
    
    if chapter.order > 2:
        if not request.user.is_authenticated:
            return redirect("login")
        if not is_user_has_access(request.user,usubsc,course,subsc):
            return render(request, 'subscriptions/subscription_list.html')
    return render(request, 'chapters/chapter_details.html', {'chapter': chapter,'chapters':chapters,'lessons':lessons})


"""
    if chapter.order < 2:
        print("Mail If Part")
        if request.user.is_authenticated:
            user=request.user
            uuser = Enrollment.objects.filter(user=request.user).values()
        else:
            return redirect("login")
        print("(((((((((((())))))))))))")
        print(is_user_has_access(request.user,usubsc,course,subsc))
        print("(((((((((((())))))))))))")
        if not is_user_has_access(request.user,usubsc,course,subsc):
            return render(request, 'subscriptions/subscription_list.html')
        return render(request, 'chapters/chapter_details.html', {'chapter': chapter,'chapters':chapters,'lessons':lessons})
    else:
        print("Mail Else Part")
        if not request.user.is_authenticated:
            return redirect("login")
        else:
            return render(request, 'subscriptions/subscription_list.html')
"""

def is_user_has_access(user,user_subc,course,course_subc):
    # Define access levels
    print("User :",user,"User_Subscription :",user_subc)
    print("Course :",course,"Subscription :",course_subc)
    status=False
    if user_subc==1:
        if course_subc==1:
            status=True
        elif course_subc==2 or course_subc==3:
            status=True
        else:
            status=False
    elif user_subc==2:
        if course_subc==2 or course_subc==3:
            status=True
        else:
            status=False
    elif user_subc==3:
        if course_subc==1:
            status=True
        else:
            status=False
    else:
        status=False
    return status

"""
---------------------------------------------------
    if user_is_enrolled(user,subscription):
        print("Subscription:",subscription,"User:",user)
        if subscription==3:
            if course_has_subscription(course, subscription):
                print("Allow access as he has Gold subscription")            
        else:
            if subscription==2:
                if course_has_subscription(course, subscription):
                    print("Allow access as he has Silver subscription")
                else:
                    print("Course is not part of this Subscription")                    
            else:
                if subscription==1:
                    if course_has_subscription(course, subscription):
                        print("Allow access as he has Bronze subscription")
                    else:
                        print("Course is not part of this Subscription")
    else:
        print("User needs to enroll")
"""
def user_is_enrolled(user, subscription):
    return Enrollment.objects.filter(user=user, subscription=subscription).exists()

def course_has_subscription(course, subscription):
    return Course.objects.filter(title=course, subscription=subscription).exists()

@login_required
def chapter_create(request):
    if request.method == 'POST':
        form = ChapterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('chapters:chapter_list')
    else:
        form = ChapterForm()
    return render(request, 'chapters/chapter_form.html', {'form': form})

@login_required
def chapter_edit(request, slug):
    chapter = get_object_or_404(Chapter, slug=slug)
    if request.method == 'POST':
        form = ChapterForm(request.POST, instance=chapter)
        if form.is_valid():
            form.save()
            return redirect('chapters:chapter_detail', slug=chapter.slug)
    else:
        form = ChapterForm(instance=chapter)
    return render(request, 'chapters/chapter_form.html', {'form': form})
