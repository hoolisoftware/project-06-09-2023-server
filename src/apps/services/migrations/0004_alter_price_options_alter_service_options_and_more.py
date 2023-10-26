# Generated by Django 4.2.5 on 2023-10-23 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_price_starting_from'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='price',
            options={'ordering': ['id'], 'verbose_name': 'Цена', 'verbose_name_plural': 'Цены'},
        ),
        migrations.AlterModelOptions(
            name='service',
            options={'ordering': ['id'], 'verbose_name': 'Комплекс услуг', 'verbose_name_plural': 'Комплексы услуг'},
        ),
        migrations.AlterField(
            model_name='price',
            name='price',
            field=models.IntegerField(blank=True, help_text='Заметка: 0 если бесплатно, -1 что бы не показывать цену', null=True, verbose_name='Цена'),
        ),
    ]