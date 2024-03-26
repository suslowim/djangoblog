from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "users"

    def ready(self) -> None:
        """Allow usage of signals e.g. to create profile when new user is created.
        Importing a package runs all the code in the imported packagee.
        """
        import users.signals
