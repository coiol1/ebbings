# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0010_auto_20150811_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='example',
            field=models.TextField(null=True),
        ),
    ]
