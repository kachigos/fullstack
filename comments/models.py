from django.db import models
from django.contrib.auth import get_user_model
from posts.models import Post

User = get_user_model()



class Comment(models.Model):
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    product = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body