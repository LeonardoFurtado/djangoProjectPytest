from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import ProfileView

urlpatterns = [
    path('profiles/', ProfileView.as_view()),
]
