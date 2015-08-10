# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_auto_20150810_1750'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='GroupDeck',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('deadline', models.DateTimeField()),
                ('weight', models.IntegerField()),
                ('deck', models.ForeignKey(to='index.Deck')),
                ('group', models.ForeignKey(to='index.Group')),
            ],
        ),
        migrations.DeleteModel(
            name='Class',
        ),
        migrations.AddField(
            model_name='group',
            name='decks',
            field=models.ManyToManyField(to='index.Deck', through='index.GroupDeck'),
        ),
    ]
