from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from courses.models import Course
from chat.models import ChatRoom, Message
from chat.forms import MessageForm
from blogs.models import Blog

# Create your views here.
#@login_required
def home(request):
    courses = Course.objects.all()
    blogs = Blog.objects.all()
    rooms = ChatRoom.objects.all()
    room = "ikchat"
    messages = []
    room_id=1
    ############ CHAT ##############
    if room_id:
        room = ChatRoom.objects.get(id=room_id)
        messages = Message.objects.filter(room=room).order_by('timestamp')
        form = MessageForm()
        if request.method == 'POST':
            form = MessageForm(request.POST)
            if form.is_valid():
                message = form.save(commit=False)
                message.room = room
                message.user = request.user
                message.save()
                return redirect('room_detail', room_id=room_id)    
    ############ End CHAT##########
    return render(request, 'dashboard/home.html', {'courses': courses,'blogs': blogs,'rooms': rooms,'room': room,'messages': messages,})


def index(request):
    return render(request, 'dashboard/index.html')    

def contactus(request):
    return render(request, 'pages/contactus.html')  
    
def aboutus(request):
    return render(request, 'pages/aboutus.html')   

def faq(request):
    return render(request, 'pages/pages_faq.html')    

def tandc(request):
    return render(request, 'pages/terms_conditions.html')      
    
