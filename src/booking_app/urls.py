from django.urls import path, include, re_path
from .views import (
    main_view,
    info_view,
    # some_view,
    # MyView,
    # some_template_view,
    home_view,
    user_comment_view
)

urlpatterns = [
    path('main', main_view),
    path('info', info_view),
    # path('some_url/<int:some_int>/<str:some_str>', some_view),
    # re_path(r"^some_new_url/(?P<year>[0-9]{1,3})$", MyView.as_view()),
    # path('index', some_template_view),
    path('home', home_view, name="home"),
    path('user_comment', user_comment_view, name="user_comment"),

]
