from django.db import models
from django.utils import timezone


class Topping(models.Model):
    name = models.CharField(max_length=200)
    pizza = models.ForeignKey('pizzas.Pizza', null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, default=1.00)

    def __str__(self):
        return self.name

