from django import forms

from homeworks.mixins import DisabledFieldsMixin
from tests.models import Test, Answer


class AnswerBaseForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['answer']
        widgets = {
            'answer': forms.Textarea(attrs={'placeholder': 'Give your answer...'})
        }


class TestBaseForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title of the test'})
        }


class TestCreateForm(TestBaseForm):
    pass


class TestDeleteForm(DisabledFieldsMixin, TestBaseForm):
    disabled_fields = ['title']


class TestAnswerForm(AnswerBaseForm):
    pass
