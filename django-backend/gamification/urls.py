from django.urls import path
from . import views

urlpatterns = [
    path('gamification/', views.GamificationListCreateView.as_view(), name='gamification-list'),
    path('gamification/<int:pk>/', views.GamificationListCreateView.as_view(), name='gamification-detail'),
]