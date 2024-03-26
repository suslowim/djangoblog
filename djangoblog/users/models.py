from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    """Extra information about a user."""

    # One profile per user; if a user is deleted, delete their associated profile
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.jpg", upload_to="profile_pics")

    def __str__(self):
        """How the model appears when viewed in the admin console."""
        return f"{self.user.username} Profile"

    def save(self, **kwargs):
        """Resize profile image on save, overriding base Model class save method."""
        super().save(**kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
