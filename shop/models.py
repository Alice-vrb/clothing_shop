from django.db import models
from django.utils import timezone

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=200)
    in_stock = models.BooleanField(default=True)
    created_at = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name

