# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0008_card_example'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='back_additional',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='card',
            name='front_additional',
            field=models.TextField(null=True),
        ),
    ]
