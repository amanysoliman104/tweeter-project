# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-27 21:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0006_auto_20181125_0518'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tweet',
            options={'ordering': ['-timestamp']},
        ),
    ]
