from django.contrib import admin

from homeworks.models import Homework


# Register your models here.

@admin.register(Homework)
class HomeworkAdmin(admin.ModelAdmin):
    pass
