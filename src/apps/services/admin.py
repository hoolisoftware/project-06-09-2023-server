from django.contrib import admin

from . import models


@admin.register(models.Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'price'
    )


@admin.register(models.Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        'title',
    )
