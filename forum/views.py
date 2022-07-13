from django.shortcuts import render
from .models import Room, Message

# Create your views here.


def home(request):
    room_list = Room.objects.all()
    context = {'rooms': room_list}
    return render(request, 'home.html', context)


def room(request, pk):
    room_detail = Room.objects.get(id=pk)
    context = {'room': room_detail}
    return render(request, 'room.html', context)
