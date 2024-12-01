from django.contrib.auth import get_user_model
from django.db import models
from homeworks.models import Homework

# Create your models here.
UserModel = get_user_model()


class Comment(models.Model):
    class Meta:
        indexes = [
            models.Index(fields=['uploaded_at']),  # Makes the sorting faster
        ]
        ordering = ['-uploaded_at']
    text = models.TextField(max_length=200)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    to_homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
