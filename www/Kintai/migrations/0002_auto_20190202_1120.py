# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2019-02-02 02:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Kintai', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dakokukubun',
            name='KoushinUser',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u66f4\u65b0\u30e6\u30fc\u30b6\u30fc'),
        ),
    ]
