from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, null=False)
    icon = models.CharField(max_length=255, null=False)


class Product(models.Model):
    category_id = models.IntegerField(default=1)
    name = models.CharField(max_length=255, null=False)
    description = models.TextField(null=True)
    main_image = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Owner(models.Model):
    user_id = models.IntegerField(null=False)
    product_id = models.IntegerField(null=False)
    price = models.IntegerField(null=False)

