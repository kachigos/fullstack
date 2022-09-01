from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Email is required')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.is_active = True
        user.send_activation_code()
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Email is required')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.is_active = True
        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)
        return user


class User(AbstractUser):
    email = models.EmailField(max_length=150, unique=True)
    username = models.CharField(max_length=150)
    activation_code = models.CharField(max_length=8, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def generate_activation_code(self):
        from django.utils.crypto import get_random_string
        code = get_random_string(length=8,
                                 allowed_chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
        self.activation_code = code
        self.save()

    def send_activation_code(self):
        from django.core.mail import send_mail
        self.generate_activation_code()
        activation_url = f'http://127.0.0.1:8000/account/activate/{self.activation_code}/'
        message = f'Activate your account, following this link {activation_url}'
        send_mail("Activate account", message, "green_star@gmail.com", [self.email])
