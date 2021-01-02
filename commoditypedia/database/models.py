from django.db import models
from django.contrib.auth.models import User

Male = 'M'
Female = 'F'
sex_choices = [(Male, 'Male'), (Female, 'Female')]

class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    phone_number = models.CharField(max_length=11, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='media/profile_images', blank=True)
    full_name = models.CharField(max_length=70, blank=True)
    sex = models.CharField(max_length=1, choices=sex_choices, default=Male, blank=True)
    customer = models.BooleanField(default=False, blank=True)
    job = models.CharField(max_length=70, blank=True)
    # save latitude and longitude for address
    address_lat = models.CharField(max_length=100, blank=True)
    address_lon = models.CharField(max_length=100, blank=True)
    def __str__(self):
        return f'{self.user}'

class Commodity(models.Model):
    title = models.CharField(max_length=100)
    price = models.BigIntegerField()
    image = models.ImageField(upload_to='media/commodity_images')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(default='')
    likes = models.ManyToManyField(User, related_name='commodity_posts')
    def total_likes(self):
        return self.likes.count()
    def __str__(self):
        return f'{self.user} - {self.title}'

class Comment(models.Model):
    commodity = models.ForeignKey(Commodity, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(max_length=500, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.user} - {self.body}'