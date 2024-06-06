from django.urls import path
from main.api.home import HomeView

urlpatterns = [
    path("", HomeView.as_view(), name="home_view"),
]