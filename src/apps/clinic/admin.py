from django.contrib import admin

from . import models


@admin.register(models.ClinicConfig)
class ClinicConfigAdmin(admin.ModelAdmin):
    list_display = (
        'phone',
        'email',
        'address'
    )


@admin.register(models.Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


@admin.register(models.Specialist)
class SpectialistAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'position'
    )


@admin.register(models.Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
