from django.urls import path, include, re_path
from .views import (
    user_comment_view,
    main_view,
    hotels_view,
    users_view
)

urlpatterns = [
    path('main', main_view, name="main"),
    path('hotels', hotels_view, name="hotels"),
    path('user_comment', user_comment_view, name="user_comment"),
    path('users', users_view, name="users"),

]
