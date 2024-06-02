from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.views import View
from django.shortcuts import render
from django.db import transaction
from django.urls import reverse_lazy

from .forms import HotelModelForm, UserModelForm
from .models import Person, Hotel, User, Booking, Room, HotelsComment
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, CreateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.decorators.cache import cache_page

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


# def user_comment_view(request):
#     context = {
#         "comments": comments
#     }
#     return render(
#         request=request,
#         template_name="user_comment.html",
#         context=context
#     )


class UserCommentListView(ListView):
    template_name = "user_comment.html"
    model = HotelsComment
    queryset = HotelsComment.objects.all()  # [:10]
    context_object_name = "comments"
    paginate_by = 5

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["comments"] = HotelsComment.objects.all()[:10]
    #     return context


# def main_view(request):
#     return render(
#         request=request,
#         template_name="main.html",
#     )


class MainTemplateView(TemplateView):
    template_name = "main.html"


class MainAddFormView(CreateView):
    template_name = "user_add_form.html"
    form_class = UserModelForm
    # reverse_lazy = "persons"
    success_url = "hotels"


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


# def users_view(request):
#     context = {
#         "users": users
#     }
#     return render(
#         request=request,
#         template_name="users.html",
#         context=context
#     )


# def persons_view(request):
#     context = {
#         "persons": Person.objects.all().prefetch_related("hotel_comments").prefetch_related("hobbies")
#     }
#     return render(
#         request=request,
#         template_name="persons.html",
#         context=context
#     )


class PersonListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):  # LoginRequiredMixin запрещает просмотр
    permission_required = ["booking_app.view.person"]     # страницы не аутентифицированным пользователям(перенаправляя
    login_url = "/admin/login/"                           # на admin/login); PermissionRequiredMixin
    template_name = "persons.html"
    model = Person
    queryset = Person.objects.all()  # [:10]
    context_object_name = "persons"
    paginate_by = 5


# @cache_page(timeout=60)
@login_required(login_url="/admin/login/")  # запрещает просмотр страницы не аутентифицированным пользователям
def hotels_view(request):                   # (перенаправляя на admin/login)
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


# def hotel_add(request):
#     if request.method == "POST":
#         form = HotelModelForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse("hotels"))
#     else:
#         form = HotelModelForm()
#     context = {
#         "form": form
#     }
#     return render(
#         request=request,
#         template_name="hotel_add_form.html",
#         context=context
#     )


class HotelAddFormView(CreateView):
    template_name = "hotel_add_form.html"
    form_class = HotelModelForm
    # success_url = "/hotels/"
    reverse_lazy = "hotels"
    # def form_valid(self, form):
    #     # This method is called when valid form data has been POSTed.
    #     # It should return an HttpResponse.
    #     form.send_email()
    #     return super().form_valid(form)


# def user_add(request):
#     if request.method == "POST":
#         form = UserModelForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse("users"))
#     else:
#         form = UserModelForm()
#     context = {
#         "form": form
#     }
#     return render(
#         request=request,
#         template_name="user_add_form.html",
#         context=context
#     )


class UserAddFormView(CreateView):
    template_name = "user_add_form.html"
    form_class = UserModelForm
    reverse_lazy = "persons"


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


# class HotelsCommentDeleteView(DeleteView):
#     template_name = "user_comment_del.html"
#     model = HotelsComment
#     success_url = reverse_lazy("user_comment")

