from django.urls import path
from main.api.home import home_view


urlpatterns = [
    path("", home_view, name="home_view"),
]