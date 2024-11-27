from django.urls import path, include

from tests.views import CreateTestView, TestsView, TestDeleteView

urlpatterns = [
    path('upload/', CreateTestView.as_view(), name='upload-test'),
    path('', TestsView.as_view(), name='test-list'),
    path('<int:pk>/', include([
                                path('delete/', TestDeleteView.as_view(), name='delete-test'),
    ])),
]