from django.db import models
from django.core.urlresolvers import reverse

from toppings.models import Topping

class Pizza(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    base_price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, default=5.00)


    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
