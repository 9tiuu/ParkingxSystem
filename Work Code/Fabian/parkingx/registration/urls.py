from django.urls import path
from .views import ProfileView, ProfileUpdateView

urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile_update/<int:pk>/', ProfileUpdateView.as_view(), name='profile_update'),
]