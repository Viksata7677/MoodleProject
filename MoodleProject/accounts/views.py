from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from accounts.mixins import RedirectIfLoggedInMixin
from accounts.forms import CustomUserCreationForm, CustomAuthenticationForm


# Create your views here.


class UserRegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('home')  # Redirect to home after registration

    def form_valid(self, form):  # AUTOMATICALLY LOGS IN AFTER REGISTRATION
        response = super().form_valid(form)
        login(self.request, self.object)
        return response


class CustomLoginView(RedirectIfLoggedInMixin, LoginView):
    authentication_form = CustomAuthenticationForm
