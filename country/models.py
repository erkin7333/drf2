from django.db import models
from drf_settings.decorators import i18n





@i18n
class Country(models.Model):
    name_uz = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Davlat'
        verbose_name_plural = "Davlatlar"


@i18n
class Region(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, blank=True, null=True)
    name_uz = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Viloyat"
        verbose_name_plural = "Viloyatlar"


@i18n
class District(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE, blank=True, null=True)
    name_uz = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Tuman"
        verbose_name_plural = "Tumanlar"