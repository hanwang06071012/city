# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-07-23 06:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('huntjob', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cityauthpermission',
            name='parent_node',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
