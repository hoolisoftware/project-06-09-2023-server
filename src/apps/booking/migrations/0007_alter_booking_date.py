# Generated by Django 4.2.5 on 2023-10-03 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0006_booking_session'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='date',
            field=models.DateField(verbose_name='Дата приёма'),
        ),
    ]
