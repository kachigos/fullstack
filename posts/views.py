from rest_auth.registration.views import SocialLoginView
from rest_framework import generics
from .models import Post, Like, Rating
from .serializers import PostListSerializer, PostDetailSerializer
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework import permissions


User = get_user_model()

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]
    filter_fields = ['title']
    search_fields = ['title']
    ordering_fields = ['title', 'id']


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    permission_classes = [permissions.IsAdminUser]



class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter
    permission_classes = [permissions.AllowAny]


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    permission_classes = [permissions.AllowAny]


# class RegisterAPIView(APIView):
#     permission_classes = [permissions.AllowAny]
#
#     def post(self, request):
#         serializer = RegisterSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response('Account created', 201)



@api_view(["GET"])
def toggle_like(request, p_id):
    user = request.user
    product = get_object_or_404(Post, id=p_id)

    if Like.objects.filter(user=user, product=product).exists():
        Like.objects.filter(user=user, product=product).delete()
    else:
        Like.objects.create(user=user, product=product)
    return Response("Like toggled", 200)


@api_view(["POST"])
def add_rating(request, p_id):
    user = request.user
    product = get_object_or_404(Post, id=p_id)
    value = request.POST.get("value")

    if not user.is_authenticated:
        raise ValueError("authentication credentials are not provided")

    if not value:
        raise ValueError("value is required")

    if Rating.objects.filter(user=user, product=product).exists():
        rating = Rating.objects.get(user=user, product=product)
        rating.value = value
        rating.save()
    else:
        Rating.objects.create(user=user, product=product, value=value)

    return Response("rating created", 201)