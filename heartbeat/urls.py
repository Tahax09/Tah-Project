from django.urls import path
from heartbeat import views

urlpatterns = [
    path("", views.home, name="home"),
]