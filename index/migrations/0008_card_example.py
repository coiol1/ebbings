# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0007_auto_20150810_2100'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='example',
            field=models.TextField(default='example'),
            preserve_default=False,
        ),
    ]
