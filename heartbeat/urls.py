from django.urls import path
from heartbeat import views
from heartbeat.views import HomeView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
]