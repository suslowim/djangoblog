from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # UserRegisterForm automatically knows to save to users table.
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, message="Your account has been created! You are now able to log in.")
            return redirect("login")

    else:
        form = UserRegisterForm()
    return render(request, template_name="users/register.html", context={"form": form})


@login_required
def profile(request):
    return render(request, template_name="users/profile.html")
