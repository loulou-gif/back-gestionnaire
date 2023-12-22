from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class UserDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    direction = models.CharField(max_length=50)
    numero = models.CharField(max_length=50)
    manager = models.CharField(max_length=50)


class Stock(models.Model):
    category = models.CharField(max_length=50)
    name= models.CharField(max_length=50)
    serial_number = models.CharField(max_length=20)
    location = models.CharField(max_length=50)
    quantity = models.IntegerField()
    price = models.IntegerField()
    status = models.CharField(max_length=20)
    details = models.TextField()
    image = models.ImageField(upload_to='stock/', null=True)
    
    
class stock_category(models.Model):
    name = models.CharField(max_length=50)
    details = models.TextField()   
    
class status_product(models.Model):
    name = models.CharField(max_length=50)
    identifiant = models.IntegerField()
    details = models.TextField()
    
class direction(models.Model):
    direction =models.CharField(max_length=50)
    manager=models.CharField(max_length=50)
    
class Location(models.Model):
    name = models.CharField(max_length=50)
    details = models.TextField()