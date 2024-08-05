from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Address(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    full_name=models.CharField(max_length=125)
    house_address=models.CharField(max_length=250)
    street_address=models.CharField(max_length=300)
    landmark=models.CharField(max_length=155)
    city=models.CharField(max_length=155)
    state=models.CharField(max_length=155)
    country=models.CharField(max_length=155)
    zip=models.CharField(max_length=10)
    mobile=models.CharField(max_length=10)
    
    def __str__(self):
        return self.full_name+","+self.house_address+","+self.street_address+","+self.landmark+","+self.city+","+self.state+","+self.country+","+self.zip+","+self.mobile
