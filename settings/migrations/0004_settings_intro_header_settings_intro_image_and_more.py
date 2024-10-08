# Generated by Django 5.0.6 on 2024-06-17 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0003_slider'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='intro_header',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='settings',
            name='intro_image',
            field=models.ImageField(blank=True, null=True, upload_to='files'),
        ),
        migrations.AddField(
            model_name='settings',
            name='intro_text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
