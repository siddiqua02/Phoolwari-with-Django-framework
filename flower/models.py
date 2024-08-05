from django.db import models
from user.models import Address
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=255)
    image = models.ImageField(upload_to="category_images")
    about=models.CharField(max_length=1000,default='good flower')
    def __str__(self):
        return self.category

    class Meta:
        verbose_name_plural = "Categories"


class Flower(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    type_option=[('Artificial','Artificial'),
                 ('Natural','Natural')
                 ]
    type=models.CharField(max_length=20,choices=type_option)
    name = models.CharField(max_length=255)
    price = models.FloatField()
    
    seasonality_option = [
        ('all','all'),
        ('Spring','Spring'),
        ('Summer','Summer'),
        ('Autumn','Autumn'),
        ('Winter','Winter')
    ]

    seasonality=models.CharField(max_length=20,choices=seasonality_option)
    description = models.TextField()
    is_available = models.BooleanField(default=True)
    image = models.ImageField(upload_to="flower_images")
    vase_life=models.CharField(max_length=100)
    origin=models.CharField(max_length=100,default='india')
    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS_OPTION=[
        ("placed","placed"),
        ("packed","packed"),
        ("shipped","shipped"),
        ("delivered","delivered"),
        ("canceled","canceled")
    ]
    PAYMENT_MODE=[
        ("cod","cod"),
        ("online","online")
    ]
    user=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    flower=models.ForeignKey(Flower,on_delete=models.DO_NOTHING)
    address=models.ForeignKey(Address,on_delete=models.DO_NOTHING)
    quantity=models.IntegerField()
    price=models.FloatField()
    status=models.CharField(max_length=20,choices=STATUS_OPTION,default='placed')
    payment_method=models.CharField(max_length=20,choices=STATUS_OPTION)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField( auto_now=True)
    
    def __str__(self):
        return self.user+" "+self.status