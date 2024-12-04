from django.contrib import admin

from homeworks.models import Homework


# Register your models here.

@admin.register(Homework)
class HomeworkAdmin(admin.ModelAdmin):
    list_display = ('student', 'title', 'uploaded_at', 'is_graded')
    list_filter = ('uploaded_at',)
    ordering = ('-uploaded_at',)
