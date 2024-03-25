from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    """Adding extra fields to stock UserCreationForm."""
    email = forms.EmailField()

    class Meta:
        """Contains form meta information."""
        # The model to save the form input to.
        model = User
        # The fields to display in the form.
        fields = ["username", "email", "password1", "password2"]
