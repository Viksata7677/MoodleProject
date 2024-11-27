from django import forms

from homeworks.mixins import DisabledFieldsMixin
from tests.models import Test


class TestBaseForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ['title']


class TestCreateForm(TestBaseForm):
    pass


class TestDeleteForm(DisabledFieldsMixin, TestBaseForm):
    disabled_fields = ['title']
