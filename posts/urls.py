from django.urls import path
from .views import PostList, PostDetail, add_rating
from django.urls import path
# from .views import RegisterAPIView

# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )


urlpatterns = [
    path('<int:pk>/', PostDetail.as_view()),
    path('post_list/', PostList.as_view()),
    path('add_rating/<int:p_id>/', add_rating),
    # path('register/', RegisterAPIView.as_view()),
    # path('api/token/', TokenObtainPairView.as_view()),
    # path('api/token/refresh/', TokenRefreshView.as_view()),
]





