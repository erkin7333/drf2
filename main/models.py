from django.db import models
from drf_settings.decorators import i18n
from drf_settings.helpers import UploadTo



@i18n
class Category(models.Model):
    name_uz = models.CharField(max_length=60)
    name_en = models.CharField(max_length=60)
    image = models.ImageField(upload_to=UploadTo('category/'), blank=True, null=True, default=None)


@i18n
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    name_uz = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100)
    image = models.ImageField(upload_to=UploadTo('product'), blank=True, null=True, default=None)
    price = models.BigIntegerField()
    available = models.IntegerField(default=0, verbose_name="Bazadagisoni")
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
