# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='price',
            field=models.CharField(null=True, max_length=50, blank=True),
        ),
    ]
