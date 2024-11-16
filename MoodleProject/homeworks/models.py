from django.db import models

from accounts.models import Student


# Create your models here.


class Homework(models.Model):
    # student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='homework')
    title = models.CharField(max_length=100)
    image_url = models.URLField()
    image = models.ImageField(upload_to='homework/', blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    grade = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        blank=True, null=True)
    is_graded = models.BooleanField(default=False)
    description = models.TextField(max_length=200, blank=True, null=True)
