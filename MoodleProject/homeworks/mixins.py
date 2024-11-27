from django.http import HttpResponseForbidden


class PlaceholderMixin:
    placeholders = {}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, placeholder in self.placeholders.items():
            if field_name in self.fields:
                self.fields[field_name].widget.attrs['placeholder'] = placeholder


class DisabledFieldsMixin:
    disabled_fields = []  # List of field names to disable

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.disabled_fields:
            if field_name in self.fields:
                self.fields[field_name].disabled = True
