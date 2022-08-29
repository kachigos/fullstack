from django.contrib import admin
from .models import Post, Like, Rating, Favorite

admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Rating)
admin.site.register(Favorite)