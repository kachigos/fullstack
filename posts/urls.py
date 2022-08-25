from django.urls import path
from .views import PostList, PostDetail, add_rating

urlpatterns = [
    path('<int:pk>/', PostDetail.as_view()),
    path('', PostList.as_view()),
    path('add_rating/<int:p_id>/', add_rating),
]

