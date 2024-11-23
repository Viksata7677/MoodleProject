from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class NameValidator:
    def __init__(self, message=None):
        self.message = message

    def __call__(self, value, *args, **kwargs):
        if not value.isalpha():
            raise ValidationError(self.message)
