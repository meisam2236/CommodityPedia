from django.contrib import admin
from .models import CustomUser, Commodity, Comment

admin.site.register(CustomUser)
admin.site.register(Commodity)
admin.site.register(Comment)