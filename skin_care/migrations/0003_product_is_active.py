# Generated by Django 5.0.6 on 2024-06-27 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skin_care', '0002_product_descriptions'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
