# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0012_auto_20150812_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupdeck',
            name='deadline',
            field=models.DateTimeField(),
        ),
    ]
