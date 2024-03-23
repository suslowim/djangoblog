from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts = [
    {
        "author": "MaxS",
        "title": "Blog Post 1",
        "content": "This is my first post!",
        "date_posted": "January 1, 2024"
    },
{
        "author": "AndrewT",
        "title": "Blog Post 2",
        "content": "Second Post",
        "date_posted": "January 3, 2024"
    },
]


def home(request):
    context = {
        "posts": posts
    }
    return render(request, template_name='blog/home.html', context=context)


def about(request):
    return render(request, template_name='blog/about.html', context={"title": "About"})
