from django.db import models
from django.utils import timezone


class Topping(models.Model):
    name = models.CharField(max_length=200)
    pizza = models.ForeignKey('pizzas.Pizza', null=True, blank=True)
    

    def __str__(self):
        return self.name

