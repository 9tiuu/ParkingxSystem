from django.urls import path
from .views import ProfileUpdateView 
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('profile/', ProfileUpdateView.as_view(), name='profile'),
]