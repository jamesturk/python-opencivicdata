# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-08-17 19:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("elections", "0002_auto_20170731_2047")]

    operations = [
        migrations.RenameField(
            model_name="electionsource", old_name="event", new_name="election"
        )
    ]
