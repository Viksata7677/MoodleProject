from django import forms
from common.mixins import DisabledFieldsMixin, PlaceholderMixin
from tests.models import Test, Answer


class AnswerBaseForm(PlaceholderMixin, forms.ModelForm):
    placeholders = {
        'answer': 'Give your answer...',
    }

    class Meta:
        model = Answer
        fields = ['answer']


class TestBaseForm(PlaceholderMixin, forms.ModelForm):
    placeholders = {
        'title': 'Enter the homework title...',
    }

    class Meta:
        model = Test
        fields = ['title']


class TestCreateForm(TestBaseForm):
    pass


class TestDeleteForm(DisabledFieldsMixin, TestBaseForm):
    disabled_fields = ['title']


class TestAnswerForm(AnswerBaseForm):
    pass
