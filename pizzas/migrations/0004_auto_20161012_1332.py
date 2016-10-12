# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0003_auto_20161011_1941'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pizza',
            old_name='price',
            new_name='base_price',
        ),
    ]
