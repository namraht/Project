# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-27 20:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0015_auto_20160927_1622'),
    ]

    operations = [
        migrations.RenameField(
            model_name='repairerrating',
            old_name='username',
            new_name='r_username',
        ),
    ]