from django.conf import settings
from django.db import models


class Products(models.Model):
    "Generated Model"
    p_name = models.CharField(
        max_length=256,
    )
    mrp = models.FloatField()
