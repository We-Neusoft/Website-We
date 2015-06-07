# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iptv', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='point',
            name='sound',
            field=models.IntegerField(default=2, verbose_name='\u58f0\u9053\u6570'),
            preserve_default=False,
        ),
    ]
