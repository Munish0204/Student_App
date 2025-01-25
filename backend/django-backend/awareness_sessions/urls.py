from django.urls import path
from . import views

urlpatterns = [
    path('sessions/', views.SessionListCreateView.as_view(), name='session-list-create'),
    path('sessions/<int:pk>/', views.SessionRetrieveUpdateDestroyView.as_view(), name='session-detail'),
]