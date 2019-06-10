from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.poll_view, name="polls"),
]
