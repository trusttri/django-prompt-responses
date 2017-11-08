# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-07 11:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prompt_responses', '0003_auto_20171107_0534'),
    ]

    operations = [
        migrations.AddField(
            model_name='prompt',
            name='user_unique',
            field=models.BooleanField(default=False, verbose_name='allow only one response per user per prompt'),
        ),
    ]