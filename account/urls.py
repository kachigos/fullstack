from django.urls import path
from .views import RegisterAPIView
from django.contrib.auth import views as auth_views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register/', RegisterAPIView.as_view()),
    # path('activate/<str:activation_code>/', activate),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    # path('api/change-password/', ChangePasswordView.as_view(), name='change-password'),

]
