from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def some_view(request):
    return HttpResponse("<h1> hello django app </h1>")


def main_view(request):
    return HttpResponse("<h1> rules of friender </h1>")


def info_view(request):
    return HttpResponse("<h1> information about establishments  </h1>")
