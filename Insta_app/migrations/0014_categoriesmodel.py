# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-31 18:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Insta_app', '0013_auto_20170731_0615'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriesModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_text', models.CharField(max_length=1000)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Insta_app.PostModel')),
            ],
        ),
    ]