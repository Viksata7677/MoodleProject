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
            teacher_group, _ = Group.objects.get_or_create(name="Teacher")
            instance.groups.add(teacher_group)
            permission = Permission.objects.get(codename='can_grade_homeworks')
            instance.user_permissions.add(permission)

        elif instance.role == 'student':
            Student.objects.create(user=instance)
            student_group, _ = Group.objects.get_or_create(name="Student")
            instance.groups.add(student_group)
