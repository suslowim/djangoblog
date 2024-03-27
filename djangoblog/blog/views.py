from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post


def home(request):
    context = {"posts": Post.objects.all()}
    return render(request, template_name="blog/home.html", context=context)


class PostListView(ListView):
    """List of all blog posts."""

    model = Post
    # Name of variable to iterate over - matches the one in the template.
    # If not set, the default variable is 'object_list'.
    context_object_name = "posts"
    # Default is <app>/<model_<view type>.html
    template_name = "blog/home.html"
    # Ordering newest to oldest (inverse of date_posted ordering.)
    ordering = ["-date_posted"]


class PostDetailView(DetailView):
    """List of all blog posts

    Will look for template according to format <app>/<model_<view type>.html
    So this template is looking for blog/post_detail.html
    Name of the variable in the template has been changed to object, so
    context_object_name does not need to be defined.
    """

    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    """Form to create a new post.

    Will look for template according to format <app>/<model>_form.html
    Model is suffixed with 'form' as the same template is shared between
    the update AND create views.
    Fields variable is the fields we want to include in the form.
    """

    model = Post
    fields = ["title", "content"]

    def form_valid(self, form):
        """On submit, set the author ID on the form to the currently logged-in user."""
        form.instance.author = self.request.user
        # Run the rest of the stock form validations.
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Form to update an existing post.

    Will look for template according to format <app>/<model>_form.html
    Model is suffixed with 'form' as the same template is shared between
    the update AND create views.
    Fields variable is the fields we want to include in the form.
    """

    model = Post
    fields = ["title", "content"]

    def form_valid(self, form):
        """On submit, set the author ID on the form to the currently logged-in user."""
        form.instance.author = self.request.user
        # Run the rest of the stock form validations.
        return super().form_valid(form)

    def test_func(self):
        """Test if the currently logged-in user is the author of the post."""
        # Get the post being edited
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Delete an existing post

    Will look for template according to format <app>/<model_confirm_delete.html
    So this template is looking for blog/post_detail.html
    Name of the variable in the template has been changed to object, so
    context_object_name does not need to be defined.
    """

    model = Post
    success_url = "/"

    def test_func(self):
        """Test if the currently logged-in user is the author of the post."""
        # Get the post being edited
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, template_name="blog/about.html", context={"title": "About"})
