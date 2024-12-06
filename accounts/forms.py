from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django import forms

from accounts.models import CustomUser
from common.mixins import PlaceholderMixin


class CustomUserCreationForm(PlaceholderMixin, UserCreationForm):
    placeholders = {
        'username': 'Your username...',
        'email': 'Enter a valid email address...',
        'age': 'Enter your age...',
        'password1': 'Enter a strong password',
        'password2': 'Confirm your password',
    }

    class Meta(UserCreationForm.Meta):
        model = get_user_model()  # Should name our extended user, because django works with the base user (USER)
        fields = ('username', 'email', 'age', 'role')  # password is always included


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = '__all__'


class CustomAuthenticationForm(PlaceholderMixin, AuthenticationForm):
    placeholders = {
        'username': 'Enter email or username',
        'password': 'Enter your password',
    }


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'age', 'role']


class ProfileEditForm(ProfileBaseForm):
    class Meta(ProfileBaseForm.Meta):
        fields = ['first_name', 'last_name', 'age']


class ProfileDeleteForm(ProfileBaseForm):
    pass

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False
            field.widget.attrs['disabled'] = True
