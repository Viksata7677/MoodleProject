from django import forms
from common.mixins import PlaceholderMixin
from common.models import Comment


class CommentForm(PlaceholderMixin, forms.ModelForm):
    placeholders = {
        'text': 'Enter your comment...',
    }

    class Meta:
        model = Comment
        fields = ('text',)

