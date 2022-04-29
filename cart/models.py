from django.db import models
from main.models import Product
from country.models import Country, Region, District
from account.models import User

class DeliveryAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    zip = models.CharField(max_length=10)



class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    delivery_address = models.ForeignKey(DeliveryAddress, on_delete=models.CASCADE)
    total_price = models.BigIntegerField()
    order_at = models.DateTimeField(auto_now_add=True)

    @property
    def products(self):
        return []



class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.BigIntegerField(default=0)
    quantity = models.IntegerField()


