from django.db import models
from django.contrib.auth.models import User
from main.models import Product

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mem_name = models.CharField(max_length = 10, null=True)
    mem_nickname = models.CharField(max_length=10, null=True)
    mem_email = models.EmailField(null=True)
    mem_phone = models.CharField(max_length = 25, null=True)
    mem_address = models.CharField(max_length = 50, null=True)
    like_post = models.ManyToManyField(Product, blank=True, related_name="like_user")

