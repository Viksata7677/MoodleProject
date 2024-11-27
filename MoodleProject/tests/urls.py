from django.urls import path

from tests.views import CreateTestView, TestsView

urlpatterns = [
    path('upload/', CreateTestView.as_view(), name='upload-test'),
    path('', TestsView.as_view(), name='test-list'),
]