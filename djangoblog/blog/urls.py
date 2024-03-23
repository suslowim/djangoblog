from django.urls import path
from . import views

urlpatterns = [
    # Accessing the root of /blog returns the home view.
    path("", views.home, name="blog-home"),
    path("about/", views.about, name="blog-about")
]
