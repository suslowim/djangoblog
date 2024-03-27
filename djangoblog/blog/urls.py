from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
)
from . import views


urlpatterns = [
    # Accessing the root of /blog returns the home view.
    path("", PostListView.as_view(), name="blog-home"),
    path("about/", views.about, name="blog-about"),
    # <int:pk> is an integer variable corresponding to the primary key of the post.
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/<int:pk>/update", PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete", PostDeleteView.as_view(), name="post-delete"),
    path("user/<str:username>/", UserPostListView.as_view(), name="user-posts"),
    path("post/new/", PostCreateView.as_view(), name="post-create"),
]
