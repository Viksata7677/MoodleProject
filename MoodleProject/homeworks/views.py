from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accounts.models import Student
from homeworks.forms import HomeworkCreateForm, HomeworkEditForm, HomeworkDeleteForm, HomeworkGradeForm
from homeworks.mixins import PermissionRequiredMixin
from homeworks.models import Homework


# Create your views here.

# TODO: ADD VALIDATION ERRORS WHEN A USER TRIES TO ACCESS A VIEW BUT DOESNT HAVE THE PERMISSIONS FOR IT
# EITHER WITH PermissionDenied, try-except-raise, custom errors like
#   def custom_404_view(request, exception):
#       return render(request, '404.html', status=404)


class HomeworkUploadPage(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Homework
    form_class = HomeworkCreateForm
    template_name = 'homework/homework-upload.html'
    success_url = reverse_lazy('dashboard')
    permission_required = 'homeworks.add_homework'
    permission_denied_message = "Can't upload homework as a teacher"

    def form_valid(self, form):
        form.instance.student = self.request.user.student_profile
        return super().form_valid(form)


class HomeworkDetailPage(LoginRequiredMixin, DetailView):
    model = Homework
    template_name = 'homework/homework-details.html'
    context_object_name = 'homework'


class HomeworkEditPage(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Homework
    form_class = HomeworkEditForm
    template_name = 'homework/homework-edit.html'
    permission_required = 'homeworks.change_homework'
    permission_denied_message = "Can't edit if you are not a student."

    def get_success_url(self):
        return reverse_lazy('homework-details', kwargs={'pk': self.object.pk})


class HomeworkDeletePage(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Homework
    form_class = HomeworkDeleteForm
    template_name = 'homework/homework-delete.html'
    success_url = reverse_lazy('dashboard')
    permission_required = 'homeworks.delete_homework'
    permission_denied_message = "Can't delete if you are not a student."

    def get_initial(self) -> dict:
        return self.get_object().__dict__


class HomeworkGradePage(UpdateView):
    model = Homework
    form_class = HomeworkGradeForm
    template_name = 'homework/homework-grade.html'

    def get_success_url(self):
        return reverse_lazy('homework-details', kwargs={'pk': self.object.pk})
