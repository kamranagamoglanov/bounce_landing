# Generated by Django 5.0.6 on 2024-06-27 20:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skin_care', '0011_alter_product_expired_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/%Y/%M/%d/')),
                ('car_advertisement', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='skin_care.product')),
            ],
            options={
                'verbose_name_plural': 'Add a picture',
            },
        ),
    ]
