from django.urls import path, include
from .views import some_view, main_view, info_view

urlpatterns = [
    path('some_url', some_view),
    path('main', main_view),
    path('info', info_view),
]
