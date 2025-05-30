# Generated by Django 5.0.1 on 2024-01-16 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deepapp', '0011_blogdetails_blogimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='ManagementTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.TextField(null=True)),
                ('name', models.TextField(null=True)),
                ('image', models.ImageField(null=True, upload_to='teamimg')),
                ('status', models.BooleanField(blank=True, default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
