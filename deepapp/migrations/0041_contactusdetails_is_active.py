# Generated by Django 5.0.1 on 2024-03-22 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deepapp', '0040_productdetails_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactusdetails',
            name='is_active',
            field=models.BooleanField(blank=True, default=True),
        ),
    ]
