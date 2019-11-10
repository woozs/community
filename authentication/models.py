from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin
)

from .manager import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """
    model to create users
    """
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, unique=True)

    is_amdin = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', ]

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

    def get_uerid(self):
        return User.objects.get(username=self.username).user_id
