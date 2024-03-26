from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """When a  user is saved, create a new profile for the user if it is a new user.

    When a user (User) is saved (post_save), send a signal to this
    receiver (this function with the decorator @receiver.) If the
    user is a new user (defined by created arg) then create a new profile
    linked to the instance of the user in question.
    """
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    """Save changes to the user's profile if the user is edited.

    When a user (User) is saved (post_save), send a signal to this
    receiver (this function with the decorator @receiver.) Save
    the profile linked to the user in question (instance).
    """
    instance.profile.save()
