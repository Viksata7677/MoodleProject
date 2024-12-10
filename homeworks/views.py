from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.views.generic.edit import FormMixin
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from common.forms import CommentForm
from common.mixins import PermissionRequiredMixin
from homeworks.forms import HomeworkCreateForm, HomeworkEditForm, HomeworkDeleteForm, HomeworkGradeForm
from homeworks.models import Homework
from homeworks.serializers import HomeworkSerializer


# Create your views here.
class HomeworkView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Homework
    template_name = 'homework/homeworks.html'
    context_object_name = 'homeworks'

    permission_required = 'homeworks.view_homework'
    permission_denied_message = "You don't have the permission to view the uploaded homeworks."

    def get_queryset(self):
        user = self.request.user

        if user.is_superuser or user.is_staff:
            return Homework.objects.all()

        if user.groups.filter(name='Teacher').exists():
            return Homework.objects.all()
        else:
            return Homework.objects.filter(student__user=user)


class HomeworkUploadPage(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Homework
    form_class = HomeworkCreateForm
    template_name = 'homework/homework-upload.html'
    success_url = reverse_lazy('homeworks')

    permission_required = 'homeworks.add_homework'
    permission_denied_message = "You don't have permissions to upload homeworks."

    def form_valid(self, form):
        form.instance.student = self.request.user.student_profile
        return super().form_valid(form)


class HomeworkDetailPage(LoginRequiredMixin, DetailView, FormMixin):
    model = Homework
    template_name = 'homework/homework-details.html'
    context_object_name = 'homework'
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['comment_form'] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()

        if form.is_valid():
            comment = form.save(commit=False)
            comment.to_homework = self.get_object()
            comment.user = request.user
            comment.save()
            return HttpResponseRedirect(self.request.path + f'#{self.object.pk}')

        return self.render_to_response(self.get_context_data(comment_form=form))


class HomeworkEditPage(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Homework
    form_class = HomeworkEditForm
    template_name = 'homework/homework-edit.html'

    permission_required = 'homeworks.change_homework'
    permission_denied_message = "Can't edit this homework."

    def get_success_url(self):
        return reverse_lazy('homework-details', kwargs={'pk': self.object.pk})


class HomeworkDeletePage(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Homework
    form_class = HomeworkDeleteForm
    template_name = 'homework/homework-delete.html'
    success_url = reverse_lazy('homeworks')

    permission_required = 'homeworks.delete_homework'
    permission_denied_message = "Can't delete this homework."

    def get_initial(self):
        return self.get_object().__dict__


class HomeworkGradePage(PermissionRequiredMixin, UpdateView):
    model = Homework
    form_class = HomeworkGradeForm
    template_name = 'homework/homework-grade.html'

    permission_required = 'homeworks.can_grade_homeworks'
    permission_denied_message = "You can't grade homeworks as a student."

    def get_success_url(self):
        return reverse_lazy('homework-details', kwargs={'pk': self.object.pk})


class HomeworkListAPIView(ListAPIView):
    serializer_class = HomeworkSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.is_superuser or user.is_staff:
            return Homework.objects.all()

        if user.groups.filter(name='Teacher').exists():
            return Homework.objects.all()
        else:
            return Homework.objects.filter(student__user=user)
