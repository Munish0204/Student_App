from django.urls import path
from . import views

urlpatterns = [
    path('assignments/', views.AssignmentListCreateView.as_view(), name='assignment-list-create'),
    path('assignments/<int:pk>/', views.AssignmentDetailView.as_view(), name='assignment-detail'),
]