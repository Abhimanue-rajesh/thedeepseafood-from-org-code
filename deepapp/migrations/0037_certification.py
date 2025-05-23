# Generated by Django 5.0.1 on 2024-03-13 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deepapp', '0036_productdetails_how_to_cook_productdetails_shelf_life'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='certificationimg')),
                ('status', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
