from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Store(models.Model):
    str_id = models.AutoField(primary_key=True)
    str_user = models.OneToOneField(User, on_delete=models.CASCADE)
    str_name = models.CharField(max_length=50)
    str_email = models.CharField(max_length=100)
    str_phone = models.CharField(max_length=25)
    str_address = models.CharField(max_length=200)
    str_loc_latitude = models.CharField(max_length=50, null=True)
    str_loc_longitude = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.str_name

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    str_id = models.ForeignKey(Store, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    product_image = models.ImageField(upload_to = 'images/')
    product_description = models.CharField(max_length=500)
    product_default_price = models.PositiveIntegerField()
    # detail이 설명에 나올 부분
    product_detail = models.CharField(max_length=100)
    
    WHITE = 'WH'
    PINK = 'PI'
    SKYBLUE = 'SK'
    BROWN = 'BR'
    RED = 'RE'
    PURPLE = 'PU'
    YELLOW = 'YE'
    GREEN = 'GR'
    
    COLOR = (
        (WHITE, 'White'),
        (PINK, 'Pink'),
        (SKYBLUE, 'Skyblue'),
        (BROWN, 'Brown'),
        (RED, 'Red'),
        (YELLOW, 'Yellow'),
        (GREEN, 'Green'),
    )
    product_color = models.CharField(max_length=10, choices=COLOR, default=WHITE)


    ROUND = 'R'
    SQUARE = 'S'
    HEART = 'H'

    SHAPE = (
        (ROUND, 'Round'),
        (SQUARE, 'Square'),
        (HEART, 'Heart'),
    )
    product_shape = models.CharField(max_length=10, choices=SHAPE, default=ROUND)

# 테두리, 문구, 문양, 줄무늬,
# 윗면
    product_text = models.CharField(max_length=10, blank=True)
    product_text_color = models.CharField(max_length=10, choices=COLOR, default=WHITE)

    
    # DECO = (
    #     (TEXT, 'Text'),
    #     (NONE, 'None'),
    #     (ALL, 'All'),
    # )
    # product_deco = models.BooleanField()

    like_num = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.product_name