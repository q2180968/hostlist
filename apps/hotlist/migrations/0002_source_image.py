# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-06-25 08:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotlist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='source',
            name='image',
            field=models.ImageField(default='course/default.png', upload_to='source/%Y/%m', verbose_name='封面图'),
        ),
    ]