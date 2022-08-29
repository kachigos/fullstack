from django.urls import path
from .views import Categories


urlpatterns = [
    path('categories', Categories.as_view()),
]