# Generated by Django 4.2.2 on 2023-06-15 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0003_remove_product_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='shop_app/static/shop_app/img'),
        ),
    ]
