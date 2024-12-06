from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

UserModel = get_user_model()


class EmailOrUsernameBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None:
            username = kwargs.get(UserModel.USERNAME_FIELD)

        try:
            user = UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            try:
                user = UserModel.objects.get(username=username)  # It can work without this because next backend checks for username
            except UserModel.DoesNotExist:
                return None

        if (user.check_password(password)  # Hashes the normal password and verifies it with the hash in the base
                and
                self.user_can_authenticate(user)):  # Checks if the user is active (is_active)
            return user
