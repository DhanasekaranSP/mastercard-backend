# Generated by Django 4.2.16 on 2024-09-20 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mastercard_app', '0003_rename_image_popularcards_imageurl'),
    ]

    operations = [
        migrations.AddField(
            model_name='popularcards',
            name='ctaname',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='popularcards',
            name='is_special_card',
            field=models.BooleanField(default=False),
        ),
    ]
