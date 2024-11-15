from django.contrib.auth.views import LogoutView
from django.urls import path
from accounts.views import UserRegisterView, HomePageView, CustomLoginView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]