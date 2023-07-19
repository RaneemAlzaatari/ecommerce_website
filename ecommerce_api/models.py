from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField(max_length=500)
    category = models.CharField(max_length=100)
    price = models.IntegerField()
    stock = models.IntegerField()
    condition = models.CharField(max_length=100)
    rating = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add=True)

class ProductImg(models.Model):
    productId = models.ForeignKey(Product,on_delete=models.CASCADE)
    url = models.ImageField(upload_to='products_images', blank=True, null=True)

class Cart(models.Model):
    userId = models.ForeignKey(User,on_delete=models.CASCADE)
    quantity = models.IntegerField()

class CartItem(models.Model):
    cartId = models.ForeignKey(Cart,on_delete=models.CASCADE)
    productId = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add=True)
