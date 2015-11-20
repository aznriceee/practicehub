# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datahub_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='signup',
            name='full_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='signup',
            name='preference1',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='signup',
            name='preference2',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='signup',
            name='preference3',
            field=models.CharField(max_length=50, blank=True),
        ),
    ]
