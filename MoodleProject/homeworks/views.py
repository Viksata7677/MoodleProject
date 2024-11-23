from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accounts.models import Student
from homeworks.forms import HomeworkCreateForm, HomeworkEditForm, HomeworkDeleteForm, HomeworkGradeForm
from homeworks.models import Homework


# Create your views here.

# TODO: ADD VALIDATION ERRORS WHEN A USER TRIES TO ACCESS A VIEW BUT DOESNT HAVE THE PERMISSIONS FOR IT
# EITHER WITH PermissionDenied, try-except-raise, custom errors like
#   def custom_404_view(request, exception):
#       return render(request, '404.html', status=404)


class HomeworkUploadPage(LoginRequiredMixin, CreateView):
    model = Homework
    form_class = HomeworkCreateForm
    template_name = 'homework/homework-upload.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        homework = form.save(commit=False)

        homework.student = self.request.user.student_profile

        return super().form_valid(form)


class HomeworkDetailPage(LoginRequiredMixin, DetailView):
    model = Homework
    template_name = 'homework/homework-details.html'
    context_object_name = 'homework'


class HomeworkEditPage(LoginRequiredMixin, UpdateView):
    model = Homework
    form_class = HomeworkEditForm
    template_name = 'homework/homework-edit.html'

    def get_success_url(self):
        return reverse_lazy('homework-details', kwargs={'pk': self.object.pk})


class HomeworkDeletePage(DeleteView):
    model = Homework
    form_class = HomeworkDeleteForm
    template_name = 'homework/homework-delete.html'
    success_url = reverse_lazy('dashboard')

    def get_initial(self) -> dict:
        return self.get_object().__dict__


class HomeworkGradePage(UpdateView):
    model = Homework
    form_class = HomeworkGradeForm
    template_name = 'homework/homework-grade.html'

    def get_success_url(self):
        return reverse_lazy('homework-details', kwargs={'pk': self.object.pk})
