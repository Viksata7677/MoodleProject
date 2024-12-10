from django.contrib.auth import login, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from accounts.mixins import RedirectIfLoggedInMixin
from accounts.forms import CustomUserCreationForm, CustomAuthenticationForm, ProfileEditForm, ProfileDeleteForm
from accounts.models import CustomUser

# Create your views here.

UserModel = get_user_model()


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


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = UserModel
    template_name = 'accounts/profile-details.html'


class ProfileEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = UserModel
    template_name = 'accounts/profile-edit.html'
    form_class = ProfileEditForm

    def test_func(self):  # gives 403 error when trying to edit a different user profile
        profile = get_object_or_404(CustomUser, pk=self.kwargs['pk'])
        return self.request.user == profile

    def handle_no_permission(self):
        return HttpResponseForbidden("You don't have permission to edit this profile.")

    def get_success_url(self):
        return reverse_lazy('profile-details', kwargs={'pk': self.object.pk})


class ProfileDeleteView(DeleteView):
    model = UserModel
    template_name = 'accounts/profile-delete.html'
    form_class = ProfileDeleteForm
    success_url = reverse_lazy('home')

    def get_initial(self):  # returns a dictionary of the initial data and prepopulates the form
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)
