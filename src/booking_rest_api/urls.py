from django.urls import path
from .views import (
    # hello_world,
    SomeDataViewClass,
)


urlpatterns = [
    # path('some_url_example', hello_world),
    path('some_url_example', SomeDataViewClass.as_view()),
]
