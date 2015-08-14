# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_auto_20150813_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentcard',
            name='ease_factor',
            field=models.FloatField(default=2.5),
        ),
    ]
