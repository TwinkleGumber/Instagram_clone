# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-30 22:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Insta_app', '0010_auto_20170730_2204'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CategoryModel',
            new_name='CategoriesModel',
        ),
    ]
