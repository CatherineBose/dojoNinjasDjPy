# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-24 03:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas', '0002_auto_20171024_0151'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojo',
            name='desc',
            field=models.TextField(blank=True),
        ),
    ]
