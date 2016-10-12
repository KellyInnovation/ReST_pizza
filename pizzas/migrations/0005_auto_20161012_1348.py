# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0004_auto_20161012_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='base_price',
            field=models.DecimalField(max_digits=6, null=True, default=5.0, blank=True, decimal_places=2),
        ),
    ]
