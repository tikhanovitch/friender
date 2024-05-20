from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
from django.db import transaction

from .models import Person, Hotel, User, Booking, Room

comments = [
    {
    "number": 1,
    "name": "User 1",
    "comment": "some User 1 comment",
    },
    {
    "number": 2,
    "name": "User 2",
    "comment": "some User 2 comment",
    },
    {
    "number": 3,
    "name": "User 3",
    "comment": "some User 3 comment",
    },
]


def user_comment_view(request):
    context = {
        "comments": comments
    }
    return render(
        request=request,
        template_name="user_comment.html",
        context=context
    )


def main_view(request):
    return render(
        request=request,
        template_name="main.html",
    )


hotels = [
    {
    "number": 1,
    "name": "Hotel № 1",
    "adress": "Hotel № 1 adress",
    "stars": "****",
    },
    {
    "number": 2,
    "name": "Hotel № 2",
    "adress": "Hotel № 2 adress",
    "stars": "****",
    },
    {
    "number": 3,
    "name": "Hotel № 3",
    "adress": "Hotel № 3 adress",
    "stars": "***",
    },
]


users = [
    {
    "number": 1,
    "name": "User 1",
    "age": 35,
    },
    {
    "number": 2,
    "name": "User 2",
    "age": 23,
    },
    {
    "number": 3,
    "name": "User 3",
    "age": 27,
    },
]


def users_view(request):
    context = {
        "users": users
    }
    return render(
        request=request,
        template_name="users.html",
        context=context
    )


def persons_view(request):
    context = {
        "persons": Person.objects.all().prefetch_related("hotel_comments").prefetch_related("hobbies")
    }
    return render(
        request=request,
        template_name="persons.html",
        context=context
    )


def hotels_view(request):
    context = {
        "hotels": Hotel.objects.all()
    }
    return render(
        request=request,
        template_name="hotels.html",
        context=context
    )


def hotels_delete_view(request):
    with transaction.atomic():
        users = User.objects.filter(hobbies__name="Puzzl")
        print(users)
        return HttpResponse(f"<h1> {users} </h1>")


def book_room_view(request, hotel_name, user_id, room_number):
    pass