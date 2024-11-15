from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import TemplateView
from accounts.mixins import RedirectIfLoggedInMixin
from accounts.forms import CustomUserCreationForm, CustomAuthenticationForm


# Create your views here.


class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = 'homepage.html'


class UserRegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('home')  # Redirect to home after registration

    def form_valid(self, form):  # TODO: Make a logic for the user to log in automatically after registration
        response = super().form_valid(form)
        login(self.request, self.object)
        return response


class CustomLoginView(RedirectIfLoggedInMixin, LoginView):
    authentication_form = CustomAuthenticationForm
