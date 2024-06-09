from django.urls import path, include, re_path
from .views import (
    # user_comment_view,
    # main_view,
    # persons_view,
    hotels_view,
    # users_view,
    hotels_delete_view,
    book_room_view,
    hotel_add,
    # user_add,
    UserCommentListView,
    MainTemplateView,
    PersonListView,
    # HotelAddFormView,
    UserAddFormView,
)

urlpatterns = [
    path('main', MainTemplateView.as_view(), name="main"),  # main_view
    path('hotels', hotels_view, name="hotels"),
    path('user_comment', UserCommentListView.as_view(), name="user_comment"),
    # path('users', users_view, name="users"),
    path('persons', PersonListView.as_view(), name="persons"),
    path('hotels_del', hotels_delete_view, name="hotels_del"),
    path('book_room', book_room_view, name="book_room"),
    path('hotel_add_form', hotel_add, name="hotel_add_form"),
    # path('hotel_add_form', HotelAddFormView.as_view(), name="hotel_add_form"),
    # path('user_add_form', user_add, name="user_add_form"),
    path('user_add_form', UserAddFormView.as_view(), name="user_add_form"),
]
