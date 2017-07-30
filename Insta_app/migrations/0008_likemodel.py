# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-30 08:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Insta_app', '0007_auto_20170729_1433'),
    ]

    operations = [
        migrations.CreateModel(
            name='LikeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Insta_app.PostModel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Insta_app.UserProfile')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]