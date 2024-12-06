from django.urls import path, include
from homeworks import views

urlpatterns = [
    path('upload/', views.HomeworkUploadPage.as_view(), name='homework-upload'),
    path('dashboard/', views.HomeworkView.as_view(), name='homeworks'),
    path('<int:pk>/', include([
                                path('details/', views.HomeworkDetailPage.as_view(), name='homework-details'),
                                path('edit/', views.HomeworkEditPage.as_view(), name='homework-edit'),
                                path('delete/', views.HomeworkDeletePage.as_view(), name='homework-delete'),
                                path('grade/', views.HomeworkGradePage.as_view(), name='homework-grade'),
]))]