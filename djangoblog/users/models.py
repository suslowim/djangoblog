from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """Extra information about a user."""
    # One profile per user; if a user is deleted, delete their associated profile
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.jpg", upload_to="profile_pics")

    def __str__(self):
        return f"{self.user.username} Profile"
