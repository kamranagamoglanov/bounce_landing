# Generated by Django 5.0.6 on 2024-06-27 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skin_care', '0009_alter_product_expired_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='expired_at',
            field=models.DateField(blank=True, null=True),
        ),
    ]
