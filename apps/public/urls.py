from django.urls import path

from apps.public import views

urlpatterns = [
    path("", views.home, name="home"),
]
