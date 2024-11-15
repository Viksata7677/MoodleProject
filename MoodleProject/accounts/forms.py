from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()  # Should name our extended user, because django works with the base user (USER)
        fields = ('username', 'email')  # password is always included
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Enter you username'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email address'}),
            # TODO: add placeholders for password1 and password2
        }


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = '__all__'


class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'placeholder': 'Enter your email',
        })
        self.fields['password'].widget.attrs.update({
            'placeholder': 'Enter your password',
        })