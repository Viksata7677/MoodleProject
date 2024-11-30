from django.db import models
from accounts.models import Teacher, Student


class Test(models.Model):
    title = models.CharField(max_length=30)
    created_by = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Answer(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='answers')
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)



