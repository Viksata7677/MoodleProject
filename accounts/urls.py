from django.contrib.auth.views import LogoutView
from django.urls import path, include
from accounts.views import UserRegisterView, CustomLoginView, ProfileDetailView, ProfileEditView, ProfileDeleteView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/<int:pk>/', include([
        path('details/', ProfileDetailView.as_view(), name='profile-details'),
        path('edit/', ProfileEditView.as_view(), name='profile-edit'),
        path('delete/', ProfileDeleteView.as_view(), name='profile-delete'),
    ]))
]