from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    profile_pic = models.CharField(max_length=255, default="images/profile_pic")
    is_marketer = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=11, null=False)
