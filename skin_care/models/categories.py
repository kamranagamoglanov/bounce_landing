from django.db import models


class CosmeticCategory(models.Model):
    title = models.CharField(max_length=32)

    def __str__(self) -> str:
        return f"{self.title}"