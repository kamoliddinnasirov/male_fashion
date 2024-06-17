from django.db import models
from shop.models import ProductModel
from users.models import  UserModel
from shop.abstract import BaseModel

class OrderHistory(BaseModel):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ManyToManyField(ProductModel)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    country_name = models.CharField(max_length=125)
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=6)
    email = models.EmailField(null=True)
    total_price = models.FloatField(null=True, blank=True)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"


    class Meta:
        verbose_name = 'order'
        verbose_name_plural = "orders"
