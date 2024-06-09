from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (
    # hello_world,
    SomeDataViewClass,
    # UserApiView,
    HotelOwnerApiView,
    # HotelOwnerListApiView,
    # HobbyApiView,
    HobbyListApiView,
    UserListApiView,
    UserDetail,
)


urlpatterns = [
    # path('some_url_example', hello_world),
    path('some_url_example', SomeDataViewClass.as_view()),
    # path('users', UserApiView.as_view()),
    path('users', UserListApiView.as_view()),
    # path('users/<int:pk>', UserApiView.as_view()),
    path('users/<int:pk>', UserDetail.as_view()),
    path('hotelowner', HotelOwnerApiView.as_view()),
    # path('hotelowner', HotelOwnerListApiView.as_view()),
    path('hotelowner/<int:pk>', HotelOwnerApiView.as_view()),
    # path('hobby', HobbyApiView.as_view()),
    path('hobby', HobbyListApiView.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
