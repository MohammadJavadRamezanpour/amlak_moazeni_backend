# Generated by Django 5.0.6 on 2024-08-14 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_created_at_post_publish_post_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='desc',
            field=models.TextField(default=""),
            preserve_default=False,
        ),
    ]
