from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenBlacklistView

from .views import UserCreateView, TaskListView, TaskDetailView


urlpatterns = [
    path('register/', UserCreateView.as_view(), name='user_create'),
    path('tasks/', TaskListView.as_view(), name='task_list'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('auth/login/', TokenObtainPairView.as_view(), name='login'),
    path('auth/logout/', TokenBlacklistView.as_view(), name='logout'),
    path('auth/refresh_token/', TokenRefreshView.as_view(), name='refresh_token'),
]
