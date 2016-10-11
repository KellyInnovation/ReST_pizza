# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toppings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='topping',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True, blank=True),
        ),
    ]
