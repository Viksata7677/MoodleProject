from django.http import HttpResponseForbidden


class PermissionRequiredMixin:
    permission_required = None
    permission_denied_message = None

    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm(self.permission_required):
            return HttpResponseForbidden(self.permission_denied_message)

        return super().dispatch(request, *args, **kwargs)


class DisabledFieldsMixin:
    disabled_fields = []  # List of field names to disable

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name in self.disabled_fields:
            if field_name in self.fields:
                self.fields[field_name].disabled = True


class PlaceholderMixin:
    placeholders = {}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, placeholder in self.placeholders.items():
            if field_name in self.fields:
                self.fields[field_name].widget.attrs['placeholder'] = placeholder