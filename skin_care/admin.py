from django.contrib import admin

from .models import (
    User,
    Image,
    Product,
    CosmeticCategory,
)

class ProductModelAdmin(admin.ModelAdmin):
    readonly_fields = ("expired_at",)


admin.site.register(User)
admin.site.register(CosmeticCategory)
admin.site.register(Product, ProductModelAdmin)
admin.site.register(Image)