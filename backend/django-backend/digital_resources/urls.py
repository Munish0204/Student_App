from django.urls import path
from .views import ResourceListView, ResourceDetailView, ResourceUploadView

urlpatterns = [
    path('resources/', ResourceListView.as_view(), name='resource-list'),
    path('resources/<int:pk>/', ResourceDetailView.as_view(), name='resource-detail'),
    path('resources/upload/', ResourceUploadView.as_view(), name='resource-upload'),
]