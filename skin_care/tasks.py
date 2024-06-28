from celery import shared_task

from .models import Product


@shared_task
def deactivate_product():
    products =Product.objects.filter(is_active=True)
    for product in products:
        if product.is_expires():
            product.deactivate()