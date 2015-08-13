# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('front', models.TextField()),
                ('front_additional', models.TextField(null=True)),
                ('back', models.TextField()),
                ('back_additional', models.TextField(null=True)),
                ('example', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Deck',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=256)),
            ],
        ),
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
        migrations.CreateModel(
            name='StudentCard',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('interval', models.IntegerField()),
                ('ease_factor', models.FloatField()),
                ('learning_state', models.CharField(max_length=1, choices=[(b'1', b'learning'), (b'2', b'relearning'), (b'3', b'acquired')])),
                ('card', models.ForeignKey(to='index.Card')),
                ('deck', models.ForeignKey(to='index.Deck')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('role', models.CharField(max_length=1, choices=[(b'1', b'teacher'), (b'2', b'student')])),
                ('group', models.ForeignKey(to='index.Group')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('teacher_id', models.CharField(max_length=64)),
                ('student_id', models.CharField(max_length=64)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='decks',
            field=models.ManyToManyField(to='index.Deck', through='index.GroupDeck'),
        ),
        migrations.AddField(
            model_name='group',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, through='index.UserGroup'),
        ),
        migrations.AddField(
            model_name='card',
            name='deck',
            field=models.ForeignKey(to='index.Deck'),
        ),
        migrations.AddField(
            model_name='card',
            name='students',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, through='index.StudentCard'),
        ),
    ]
