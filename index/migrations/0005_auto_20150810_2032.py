# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('index', '0004_auto_20150810_2026'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentCard',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('interval', models.IntegerField()),
                ('difficulty', models.FloatField()),
                ('learning_state', models.CharField(default=1, max_length=1, choices=[(1, b'learning'), (2, b'relearning'), (3, b'acquired')])),
                ('card', models.ForeignKey(to='index.Card')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='card',
            name='students',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, through='index.StudentCard'),
        ),
    ]
