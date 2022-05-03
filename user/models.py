from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    profile_pic = models.CharField(max_length=255)
    is_marketer = models.BooleanField(default=False)
