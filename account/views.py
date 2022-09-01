from rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from .serializers import RegisterSerializer
from rest_framework import permissions
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from rest_framework import generics
from django.shortcuts import render, redirect
from rest_framework import status


User = get_user_model()


class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter


class RegisterAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    # @swagger_auto_schema(query_serializer=RegisterSerializer)
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response('Account created', 201)

# @api_view(["GET"])
# def activate(request, activation_code):
#     user = generics.get_object_or_404(User, activation_code=activation_code)
#     user.is_active = True
#     user.activation_code = ''
#     user.save()
#     return redirect("http://127.0.0.1:3000/")


# class ChangePasswordView(generics.UpdateAPIView):
#     """
#     An endpoint for changing password.
#     """
#     serializer_class = ChangePasswordSerializer
#     model = User
#     permission_classes = (permissions.IsAuthenticated,)
#
#     def get_object(self, queryset=None):
#         obj = self.request.user
#         return obj
#
#     def update(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         serializer = self.get_serializer(data=request.data)
#
#         if serializer.is_valid():
#             # Check old password
#             if not self.object.check_password(serializer.data.get("old_password")):
#                 return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
#             # set_password also hashes the password that the user will get
#             self.object.set_password(serializer.data.get("new_password"))
#             self.object.save()
#             response = {
#                 'status': 'success',
#                 'code': status.HTTP_200_OK,
#                 'message': 'Password updated successfully',
#                 'data': []
#             }
#
#             return Response(response)
#
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)