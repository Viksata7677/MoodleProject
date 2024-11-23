from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class GradeValidator:

    def __init__(self, min_value=2, max_value=6):
        self.min_value = min_value
        self.max_value = max_value

    def __call__(self, value):
        if value < self.min_value or value > self.max_value:
            raise ValidationError(
                f'The grade must be between {self.min_value} and {self.max_value}. You entered an invalid grade: {value}.',
                params={'value': value},
            )
