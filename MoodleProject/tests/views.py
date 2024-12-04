from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, DetailView

from accounts.models import Student
from common.mixins import PermissionRequiredMixin
from tests.forms import TestCreateForm, TestDeleteForm, TestAnswerForm
from tests.models import Test, Answer


class CreateTestView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Test
    template_name = 'tests/test-create.html'
    form_class = TestCreateForm
    success_url = reverse_lazy('test-list')
    permission_required = 'tests.add_test'

    def form_valid(self, form):
        form.instance.created_by = self.request.user.teacher_profile
        return super().form_valid(form)


class TestsView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Test
    template_name = 'tests/tests.html'
    context_object_name = 'tests'
    queryset = Test.objects.all()
    permission_required = 'tests.view_test'
    permission_denied_message = "You don't have the permission to access this."


class TestDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Test
    template_name = 'tests/test-delete.html'
    form_class = TestDeleteForm
    success_url = reverse_lazy('test-list')
    permission_required = 'tests.delete_test'

    def get_initial(self) -> dict:
        return self.get_object().__dict__


class TestDetailView(LoginRequiredMixin, DetailView):
    model = Test
    template_name = 'tests/test-details.html'
    context_object_name = 'test'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        test = self.get_object()
        context['answers'] = test.answers.all()
        return context


class AnswerCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Answer
    form_class = TestAnswerForm
    template_name = 'tests/answer.html'
    success_url = reverse_lazy('test-list')
    permission_required = 'tests.add_answer'
    permission_denied_message = "You don't have the permission to answer tests."

    def form_valid(self, form):
        student = get_object_or_404(Student, user=self.request.user)
        form.instance.student = student
        form.instance.test = get_object_or_404(Test, pk=self.kwargs['pk'])

        return super().form_valid(form)