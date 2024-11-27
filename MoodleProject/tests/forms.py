from django import forms

from tests.models import Test


class TestBaseForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ['title']


class TestCreateForm(TestBaseForm):
    pass