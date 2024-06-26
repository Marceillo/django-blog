# Generated by Django 4.2.13 on 2024-06-26 08:14

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_collaboraterequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='profile_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]
