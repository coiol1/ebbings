# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0011_auto_20150811_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupdeck',
            name='deadline',
            field=models.DateField(),
        ),
    ]
