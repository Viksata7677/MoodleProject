from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class GradeValidator:

    def __init__(self, min_grade=2, max_grade=6):
        self.min_grade = min_grade
        self.max_grade = max_grade

    def __call__(self, value):
        if value < self.min_grade or value > self.max_grade:
            raise ValidationError(
                f'The grade must be between {self.min_grade} and {self.max_grade}. You entered an invalid grade: {value}.',
                params={'value': value},
            )
