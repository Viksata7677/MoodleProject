from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView
from common.mixins import PermissionRequiredMixin
from tests.forms import TestCreateForm, TestDeleteForm
from tests.models import Test


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


class TestDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Test
    template_name = 'tests/test-delete.html'
    form_class = TestDeleteForm
    success_url = reverse_lazy('test-list')
    permission_required = 'tests.delete_test'

    def get_initial(self) -> dict:
        return self.get_object().__dict__