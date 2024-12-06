from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from django.db.models.signals import post_save
from django.dispatch import receiver

from accounts.models import Teacher, Student

UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def create_profile(sender, instance, created, **kwargs):
    if created:
        if instance.role == 'teacher':
            Teacher.objects.create(user=instance)

        elif instance.role == 'student':
            Student.objects.create(user=instance)

