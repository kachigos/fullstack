from .views import PostList, PostDetail,  add_rating, favorites
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

# router.register("favorites", FavouriteViewSet)
router.register('',PostDetail)
urlpatterns = [
    path('<int:pk>', PostDetail),
    # path('list/', PostList.as_view()),
    path('add_rating/<int:p_id>/', add_rating),
    path('add_to_favorite/<int:p_id>/', favorites),
    path('', include(router.urls)),
    # path('add_to_favorites/<int:p_id>/', favorites)
]
