# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2019-02-07 03:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_auto_20190206_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.FileField(upload_to='post'),
        ),
    ]