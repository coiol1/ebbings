# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0005_auto_20150810_2032'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentcard',
            old_name='difficulty',
            new_name='ease_factor',
        ),
    ]
