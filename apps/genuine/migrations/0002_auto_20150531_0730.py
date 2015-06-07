# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('genuine', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='catalog',
            options={'ordering': ['order'], 'verbose_name': '\u5206\u7c7b', 'verbose_name_plural': '\u5206\u7c7b'},
        ),
        migrations.AlterField(
            model_name='catalog',
            name='order',
            field=models.CharField(max_length=8, verbose_name='\u6392\u5e8f'),
            preserve_default=True,
        ),
    ]
