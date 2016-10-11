from django.db import models
from django.core.urlresolvers import reverse

class Pizza(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)


    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

