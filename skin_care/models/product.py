import datetime

from django.db import models
from django.utils import timezone

from .categories import CosmeticCategory
from .photos import Image


class Product(models.Model):
    category = models.ForeignKey(CosmeticCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=64, null=True, blank=True)
    price = models.PositiveIntegerField()

    production_date = models.DateField()
    lifetime_in_days = models.PositiveSmallIntegerField(help_text="How long is the expiration date?", null=True, blank=True)
    expired_at = models.DateField(null=True, blank=True, editable=False)

    descriptions = models.TextField(max_length=350, null=True, blank=True)

    is_bestseller = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.category}: {self.name} {self.production_date}"
    
    def save(self, *args, **kwargs) -> None:
        if not self.expired_at:
            self.expired_at = self.calculate_expire_date()
        return super().save(*args, **kwargs)
    
    def is_expires(self) -> bool:
        if self.expired_at:
            return self.expired_at < timezone.now().date()

    def calculate_expire_date(self):
        return self.production_date + datetime.timedelta(days=self.lifetime_in_days)

    def deactivate(self) -> None:
        self.is_active = False
        self.save()