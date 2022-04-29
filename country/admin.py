from django.contrib import admin
from .models import Country, Region, District


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name'
    )


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name'
    )


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name'
    )