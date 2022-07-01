from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

# importing the signals to our app
    def ready(self):
        import users.signals
