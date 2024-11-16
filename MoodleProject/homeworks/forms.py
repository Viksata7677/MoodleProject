from django import forms

from homeworks.mixins import PlaceholderMixin, DisabledFieldsMixin
from homeworks.models import Homework


class HomeworkBaseForm(PlaceholderMixin, forms.ModelForm):
    class Meta:
        model = Homework
        exclude = ('owner', 'student', 'is_graded', 'grade')


class HomeworkCreateForm(HomeworkBaseForm):
    placeholders = {
        'title': 'Enter the homework title...',
        'image_url': 'Enter a valid image url...',
        'description': 'Description about your homework...',
    }


class HomeworkEditForm(PlaceholderMixin, forms.ModelForm):
    class Meta:
        model = Homework
        fields = ('title', 'image_url', 'description')


class HomeworkDeleteForm(DisabledFieldsMixin, HomeworkBaseForm):
    disabled_fields = ['title', 'image_url', 'description']


