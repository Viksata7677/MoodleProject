from django.urls import path, include

from tests.views import CreateTestView, TestsView, TestDeleteView, AnswerCreateView, TestDetailView

urlpatterns = [
    path('dashboard/', TestsView.as_view(), name='test-list'),
    path('upload/', CreateTestView.as_view(), name='upload-test'),
    path('<int:pk>/', include([path('details/', TestDetailView.as_view(), name='test-detail'),
                                    path('answer/', AnswerCreateView.as_view(), name='create-answer'),
                                    path('delete/', TestDeleteView.as_view(), name='delete-test'),
    ]))
]