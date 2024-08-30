import json

from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async

from .models import Room, Message

User = get_user_model()

import json
from channels.generic.websocket import WebsocketConsumer
from .models import Message, ChatRoom

class ChatConsumer(WebsocketConsumer):
    def fetch_messages(self, data):
        room_name = data['room_name']
        messages = Message.objects.filter(room__name=room_name).order_by('timestamp')
        content = {
            'messages': [{'user': m.user.username, 'content': m.content} for m in messages]
        }
        self.send(text_data=json.dumps(content))

    def receive(self, text_data):
        data = json.loads(text_data)
        room_name = data['room_name']
        message = data['message']
        user = self.scope['user']
        
        room, _ = ChatRoom.objects.get_or_create(name=room_name)
        Message.objects.create(user=user, room=room, content=message)
        self.send(text_data=json.dumps({
            'user': user.username,
            'message': message
        }))


"""
class ChatConsumer(AsyncWebsocketConsumer):
    print("Hello From chatConsumer")
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        print("Hello From receive function")
        data = json.loads(text_data)
        print(data)
        message = data['message']
        username = data['username']
        room = data['room']

        await self.save_message(username, room, message)

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        username = event['username']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'username': username
        }))

    @sync_to_async
    def save_message(self, username, room, message):
        user = User.objects.get(username=username)
        room = Room.objects.get(slug=room)

        Message.objects.create(user=user, room=room, content=message)


"""
