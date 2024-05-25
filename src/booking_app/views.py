from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.views import View
from django.shortcuts import render
from django.db import transaction
from django.urls import reverse

from .forms import HotelModelForm, UserModelForm
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


def hotel_add(request):
    if request.method == "POST":
        form = HotelModelForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("hotels"))
    else:
        form = HotelModelForm()
    context = {
        "form": form
    }
    return render(
        request=request,
        template_name="hotel_add_form.html",
        context=context
    )


def user_add(request):
    if request.method == "POST":
        form = UserModelForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("users"))
    else:
        form = UserModelForm()
    context = {
        "form": form
    }
    return render(
        request=request,
        template_name="user_add_form.html",
        context=context
    )




def book_room_view(request, hotel_id, user_id, room_number):
    hotel = Hotel.objects.get(pk=hotel_id)
    room = Room.objects.get(hotel=hotel, number=room_number)

    if room.is_booked:
        return HttpResponse("Room is already booked.", status=400)

    with transaction.atomic():
        booking = Booking.objects.create(
            start_date=request.POST['start_date'],
            end_date=request.POST['end_date'],
            customer_full_name=f"{request.POST['first_name']} {request.POST['last_name']}",
            room=room,
            user_id=user_id
        )

    room.is_booked = True
    room.save()

    return HttpResponse("Booking successful")

