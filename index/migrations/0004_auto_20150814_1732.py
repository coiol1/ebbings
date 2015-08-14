# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_auto_20150814_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentcard',
            name='interval',
            field=models.IntegerField(default=1440),
        ),
    ]
