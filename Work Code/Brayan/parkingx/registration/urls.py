from django.urls import path
from .views import ProfileView, ProfileUpdateView

urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
    # URL PROFILE UPDATE
]