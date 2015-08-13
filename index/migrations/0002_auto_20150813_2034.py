# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentcard',
            name='due',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='studentcard',
            name='ease_factor',
            field=models.FloatField(default=1.0),
        ),
        migrations.AlterField(
            model_name='studentcard',
            name='interval',
            field=models.IntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='studentcard',
            name='learning_state',
            field=models.CharField(default=b'1', max_length=1, choices=[(b'1', b'learning'), (b'2', b'relearning'), (b'3', b'acquired')]),
        ),
    ]
