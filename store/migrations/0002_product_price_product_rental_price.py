# Generated by Django 5.0.6 on 2024-06-19 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='rental_price',
            field=models.IntegerField(default=0),
        ),
    ]
