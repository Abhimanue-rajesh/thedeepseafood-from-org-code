# Generated by Django 5.0.1 on 2024-03-22 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deepapp', '0044_enquirydetails_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventgalleryimage',
            name='is_active',
            field=models.BooleanField(blank=True, default=True),
        ),
    ]
