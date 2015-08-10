# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0006_auto_20150810_2043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentcard',
            name='learning_state',
            field=models.CharField(default=1, max_length=1, choices=[(b'1', b'learning'), (b'2', b'relearning'), (b'3', b'acquired')]),
        ),
        migrations.AlterField(
            model_name='usergroup',
            name='role',
            field=models.CharField(max_length=1, choices=[(b'1', b'teacher'), (b'2', b'student')]),
        ),
    ]
