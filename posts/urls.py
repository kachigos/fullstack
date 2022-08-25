from django.urls import path
from .views import PostList, PostDetail, add_rating, RegisterAPIView

urlpatterns = [
    path('<int:pk>/', PostDetail.as_view()),
    path('post_list/', PostList.as_view()),
    path('add_rating/<int:p_id>/', add_rating),
    path('register/', RegisterAPIView.as_view()),
]

