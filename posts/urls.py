from django.urls import path
from . import views

urlpatterns = [
    path("posts/", views.post_view, name="post"),
    path("posts/list/", views.post_list_view, name="post_list")
]
