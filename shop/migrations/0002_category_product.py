# Generated by Django 5.1.4 on 2024-12-08 10:19

import django.db.models.deletion
import shop.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('image', models.ImageField(null=True, upload_to=shop.models.getFileName)),
                ('description', models.TextField(max_length=500)),
                ('status', models.BooleanField(default=False, help_text='0-Show,1-Hidden')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('vendor', models.CharField(max_length=150)),
                ('product_image', models.ImageField(null=True, upload_to=shop.models.getFileName)),
                ('quantity', models.IntegerField()),
                ('original_price', models.FloatField()),
                ('selling_price', models.FloatField()),
                ('description', models.TextField(max_length=500)),
                ('status', models.BooleanField(default=False, help_text='0-Show,1-Hidden')),
                ('trending', models.BooleanField(default=False, help_text='0-Default,1-Trending')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.category')),
            ],
        ),
    ]
