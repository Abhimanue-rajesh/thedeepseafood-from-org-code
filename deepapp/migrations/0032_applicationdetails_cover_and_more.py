# Generated by Django 5.0.1 on 2024-01-29 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deepapp', '0031_product_canonical_product_keyword_product_metatag_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationdetails',
            name='cover',
            field=models.FileField(null=True, upload_to='careerfiles'),
        ),
        migrations.AlterField(
            model_name='applicationdetails',
            name='attachment',
            field=models.FileField(null=True, upload_to='careerfiles'),
        ),
    ]
