# Generated by Django 4.2.5 on 2023-09-28 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='service',
            options={'verbose_name': 'Комплекс услуг', 'verbose_name_plural': 'Комплексы услуг'},
        ),
    ]
