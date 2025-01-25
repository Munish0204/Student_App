from django.urls import path
from . import views

urlpatterns = [
    path('gamification/', views.GamificationList.as_view(), name='gamification-list'),
    path('gamification/<int:pk>/', views.GamificationDetail.as_view(), name='gamification-detail'),
]