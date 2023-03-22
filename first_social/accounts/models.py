from django.db import models
from django.contrib.auth import models as auth_models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(auth_models.User, auth_models.PermissionsMixin):

    def __str__(self):
        return f"@{self.username}"
