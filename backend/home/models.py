from django.conf import settings
from django.db import models


class Products(models.Model):
    "Generated Model"
    p_name = models.CharField(
        max_length=256,
    )
    mrp = models.FloatField()
    image = models.CharField(
        null=True,
        blank=True,
        max_length=256,
    )
    seller = models.OneToOneField(
        "users.User",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="products_seller",
    )
