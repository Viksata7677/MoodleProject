from django.contrib import admin

from tests.models import Test, Answer


# Register your models here.

@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_by', 'created_at')
    ordering = ('-created_at',)


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('test', 'answer', 'student', 'created_at')
    ordering = ('-created_at',)