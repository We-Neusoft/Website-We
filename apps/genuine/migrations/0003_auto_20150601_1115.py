# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('genuine', '0002_auto_20150531_0730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalog',
            name='order',
            field=models.IntegerField(verbose_name='\u6392\u5e8f'),
            preserve_default=True,
        ),
    ]
