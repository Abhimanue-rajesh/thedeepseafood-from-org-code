# Generated by Django 5.0.1 on 2024-03-22 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deepapp', '0043_contactusdetails_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='enquirydetails',
            name='is_active',
            field=models.BooleanField(blank=True, default=True),
        ),
    ]
