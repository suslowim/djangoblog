from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    """Post model containing blog post information."""

    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Return the absolute URL of a specific post."""
        # Go to the post detail view, passing the primary key of the post.
        return reverse(viewname="post-detail", kwargs={"pk": self.pk})
