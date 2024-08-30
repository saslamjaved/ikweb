from django.shortcuts import render, redirect
from .models import ChatRoom, Message
from .forms import MessageForm
from django.contrib.auth.decorators import login_required

@login_required
def room_list(request):
    rooms = ChatRoom.objects.all()
    return render(request, 'chat/room_list.html', {'rooms': rooms})

@login_required
def room_detail(request, room_id):
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
    
    return render(request, 'chat/room_detail.html', {
        'room': room,
        'messages': messages,
        'form': form
    })
