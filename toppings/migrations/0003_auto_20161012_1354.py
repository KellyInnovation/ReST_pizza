# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toppings', '0002_topping_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topping',
            name='price',
            field=models.DecimalField(decimal_places=2, default=1.0, blank=True, max_digits=6, null=True),
        ),
    ]
