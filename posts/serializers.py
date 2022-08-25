from rest_framework import serializers
from .models import Post, Like, Rating
from django.contrib.auth import get_user_model

User = get_user_model()


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'price', 'image', 'category')


class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    def to_representation(self, instance: Post):
        rep = super().to_representation(instance)
        # rep["comments"] = CommentSerializer(instance.comments.all(), many=True).data
        rep["likes"] = instance.likes.all().count()
        rep["rating"] = instance.get_average_rating()
        # rep["liked_by_user"] = False
        # rep["user_rating"] = 0
        # rep["favorites"] = instance.favorites.all().count()
        # rep["favorite_by_user"] = False
        # rep['images'] = ProductImageSerializer(instance.image.all(),many=True, context=self.context).data
        request = self.context.get("request")

        if request.user.is_authenticated:
            rep["liked_by_user"] = Like.objects.filter(user=request.user, product=instance).exists()
            # if Rating.objects.filter(user=request.user, product=instance).exists():
            #     rating = Rating.objects.get(user=request.user, product=instance)
            #     rep["user_rating"] = rating.value

        return rep


class RegisterSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField()

    class Meta:
        model = User
        fields = [
            'email', 'username', 'password',
            'password_confirm'
        ]

    def validate_email(self, email):
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError('User with this email already exist')
        return email

    def validate(self, attrs):
        p1 = attrs['password']
        p2 = attrs.pop('password_confirm')

        if p1 != p2:
            raise serializers.ValidationError(
                'Password does not match'
            )
        return attrs

    def create(self, validated_data):
        print("create user with data:", validated_data)
        return User.objects.create_user(**validated_data)