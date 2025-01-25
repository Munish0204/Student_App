from django.urls import path
from .views import LanguagePreferenceList, LanguagePreferenceDetail

urlpatterns = [
    path('preferences/', LanguagePreferenceList.as_view(), name='language-preference-list'),
    path('preferences/<int:pk>/', LanguagePreferenceDetail.as_view(), name='language-preference-detail'),
]