from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("posts/", views.posts, name="posts"),
    path('posts/<slug:slug>', views.view_post, name="view-post")

]