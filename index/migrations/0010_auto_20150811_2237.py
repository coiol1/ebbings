# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0009_auto_20150811_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deck',
            name='name',
            field=models.CharField(unique=True, max_length=256),
        ),
    ]
