from django.db import models

from accounts.models import Student
from homeworks.validators import GradeValidator


# Create your models here.


class Homework(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='homework')
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to='homework_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    grade = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        validators=[GradeValidator()],
        blank=True, null=True)
    is_graded = models.BooleanField(default=False)
    description = models.TextField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):

        self.is_graded = self.grade is not None
        super().save(*args, **kwargs)

        self.student.update_avg_grade()

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        self.student.update_avg_grade()

    class Meta:
        permissions = [
            ('can_grade_homeworks', 'Can grade homeworks'),
        ]


