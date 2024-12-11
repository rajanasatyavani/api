from django.urls import path
from .views import get_users, create_user, user_detail

urlpatterns = [
    path('user/create/', create_user, name='create_user'),  # Create user
    path('users/', get_users, name='get_users'),  # Get all users
    path('user/<int:pk>/', user_detail, name='user_detail'),  # User detail by ID
]
