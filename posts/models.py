from django.db import models
from category.models import Category
from django.contrib.auth import get_user_model


User = get_user_model()

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    image = models.ImageField(upload_to='images', null=True, blank=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_average_rating(self):
        ratings = [rating.value for rating in self.ratings.all()]
        if ratings:
            return sum(ratings) / len(ratings)
        return 0


class Like(models.Model):
    user = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
    product = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.product)

class Rating(models.Model):
    user = models.ForeignKey(User, related_name='ratings', on_delete=models.CASCADE)
    product = models.ForeignKey(Post, related_name='ratings', on_delete=models.CASCADE)
    value = models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])

    def __str__(self):
        return str(self.value)

class Favorite(models.Model):
    user = models.ForeignKey(User, related_name='favorites', on_delete=models.CASCADE)
    product = models.ForeignKey(Post, related_name='favorites', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.product)