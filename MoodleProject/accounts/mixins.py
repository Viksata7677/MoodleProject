from django.shortcuts import redirect


class RedirectIfLoggedInMixin:

    redirect_url = 'home'  # Redirects to that view when the user tries to access a view meant for non-authenticated
                                                        # users

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.redirect_url)
        return super().dispatch(request, *args, **kwargs)
