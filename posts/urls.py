from .views import PostList, PostDetail,PostCRUD, FavouriteViewSet, add_rating, favorites
from django.urls import path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("favorites", FavouriteViewSet)

urlpatterns = [
    path('detail/<int:pk>/', PostDetail.as_view()),
    path('postCRUD/',PostCRUD.as_view()),
    path('post_list/', PostList.as_view()),
    path('add_rating/<int:p_id>/', add_rating),
    path('add_to_favorite/<int:s_id>/', favorites),
]





