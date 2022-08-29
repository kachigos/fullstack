from django.db import models
from django.contrib.auth import get_user_model
from posts.models import Post


User = get_user_model()

STATUS_CHOICES = (
    ('open', 'Открыт'),
    ('in_process', 'В обработке'),
    ('closed', 'Закрыт')
)


class OrderItem(models.Model):
    order = models.ForeignKey('Order', related_name='items', on_delete=models.RESTRICT)
    product = models.ForeignKey(Post, on_delete=models.RESTRICT)
    quantity = models.SmallIntegerField(default=1)


class Order(models.Model):
    user = models.ForeignKey(User, related_name='orders', on_delete=models.RESTRICT)
    product = models.ManyToManyField(Post, through=OrderItem)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)