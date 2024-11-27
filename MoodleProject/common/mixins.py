from django.http import HttpResponseForbidden


class PermissionRequiredMixin:
    permission_required = None
    permission_denied_message = None

    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm(self.permission_required):
            return HttpResponseForbidden(self.permission_denied_message)
        return super().dispatch(request, *args, **kwargs)
