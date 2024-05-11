from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


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


def hotels_view(request):
    context = {
        "hotels": hotels
    }
    return render(
        request=request,
        template_name="hotels.html",
        context=context
    )


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
