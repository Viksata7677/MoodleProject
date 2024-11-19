from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView

from homeworks.models import Homework


# Create your views here.


class HomePageView(TemplateView):
    template_name = 'homepage.html'


class DashboardView(LoginRequiredMixin, ListView):
    model = Homework
    template_name = 'dashboard.html'
    context_object_name = 'homeworks'
    queryset = Homework.objects.all()