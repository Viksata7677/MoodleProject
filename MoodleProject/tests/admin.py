from django.contrib import admin

from tests.models import Test, Answer


# Register your models here.

@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    pass


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    pass