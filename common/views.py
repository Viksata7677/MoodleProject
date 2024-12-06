from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView
from common.mixins import PermissionRequiredMixin
from homeworks.models import Homework


# Create your views here.


class HomePageView(TemplateView):

    def get_template_names(self):
        if self.request.user.is_authenticated:
            return ['common/homepage-authenticated.html']

        return ['common/homepage-not-authenticated.html']


