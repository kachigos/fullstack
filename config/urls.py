"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from account.views import FacebookLogin, GoogleLogin
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from django.conf.urls.static import static
from django.conf import settings
from rest_auth.views import PasswordResetConfirmView


schema_view = get_schema_view(
    openapi.Info(
        title = 'GREEN STAR API',
        description = 'URLки  green_star',
        default_version = 'v1',
    ),
    public = True
)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/posts/', include('posts.urls')),
    path('api/v1/orders/', include('order.urls')),
    path('api/v1/account/', include('account.urls')),
    path('api/v1/comments/', include('comments.urls')),
    path('api/v1/category/', include('category.urls')),
    path('api/v1/api-auth/', include('rest_framework.urls')),
    path('api/v1/dj-rest-auth/', include('dj_rest_auth.urls')),
    # http://127.0.0.1:8000/api/v1/dj-rest-auth/login/  --> login
    # http://127.0.0.1:8000/api/v1/dj-rest-auth/logout/ --> logout
    path('docs/', schema_view.with_ui('swagger')),
    path('rest-auth/password/reset/confirm/<str:uidb64>/<str:token>', PasswordResetConfirmView.as_view(),name='password_reset_confirm'),

]

urlpatterns += [
    path('api/v1/dj-rest-auth/facebook/', FacebookLogin.as_view(), name='fb_login'),
    path('api/v1/dj-rest-auth/google/', GoogleLogin.as_view(), name='google_login')
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

