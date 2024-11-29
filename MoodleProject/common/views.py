from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView

from common.mixins import PermissionRequiredMixin
from homeworks.models import Homework


# Create your views here.


class HomePageView(TemplateView):
    template_name = 'homepage.html'


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
