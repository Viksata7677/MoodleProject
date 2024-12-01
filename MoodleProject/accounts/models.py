from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from accounts.choices import RoleChoices
from accounts.managers import AppUserManager
from accounts.validators import NameValidator


# Create your models here.


class CustomUser(AbstractBaseUser, PermissionsMixin):
    role = models.CharField(max_length=10, choices=RoleChoices.choices, null=True)
    first_name = models.CharField(max_length=20, validators=[NameValidator(message='Should contain only letters')],)
    last_name = models.CharField(max_length=20, validators=[NameValidator(message='Should contain only letters')],)
    age = models.IntegerField(null=True)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=20, unique=True)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    objects = AppUserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email


class Teacher(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='teacher_profile')

    def __str__(self):
        return self.user.username


class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='student_profile')
    avg_grade = models.FloatField(default=0.0)

    def update_avg_grade(self):
        grades = self.homework.filter(is_graded=True).values_list('grade', flat=True)

        if grades:
            self.avg_grade = sum(grades) / len(grades)
        else:
            self.avg_grade = 0.0

        self.save()

    def __str__(self):
        return self.user.username
