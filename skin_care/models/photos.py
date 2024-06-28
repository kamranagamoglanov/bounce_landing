from django.db import models


class Image(models.Model):
    product = models.ForeignKey(
        "Product",
        on_delete=models.CASCADE,
        null=True
    )
    image = models.ImageField(upload_to="images/%y/%m/%d/")
    
    def __str__(self) -> str:
        return str(self.image)

    class Meta:
        verbose_name_plural="Add a picture"