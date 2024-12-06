from django import forms
from common.mixins import DisabledFieldsMixin, PlaceholderMixin
from homeworks.models import Homework


class HomeworkBaseForm(PlaceholderMixin, forms.ModelForm):
    class Meta:
        model = Homework
        exclude = ('student', 'is_graded', 'grade',)


class HomeworkCreateForm(HomeworkBaseForm):
    placeholders = {
        'title': 'Enter the homework title...',
        'image': 'Enter a valid image url...',
        'description': 'Description about your homework...',
    }


class HomeworkEditForm(PlaceholderMixin, forms.ModelForm):
    class Meta:
        model = Homework
        fields = ('title', 'description',)


class HomeworkDeleteForm(DisabledFieldsMixin, HomeworkBaseForm):
    disabled_fields = ['title', 'image', 'description']

    class Meta(HomeworkBaseForm.Meta):
        exclude = HomeworkBaseForm.Meta.exclude + ('image',)  # Removes 'image' field when deleting a homework


class HomeworkGradeForm(PlaceholderMixin, forms.ModelForm):
    class Meta:
        model = Homework
        fields = ('grade',)


