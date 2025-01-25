from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DigitalResourceViewSet

router = DefaultRouter()
router.register(r'resources', DigitalResourceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]