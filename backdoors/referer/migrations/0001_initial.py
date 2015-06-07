# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField(verbose_name=b'URL')),
                ('enable', models.BooleanField(default=False, verbose_name=b'\xe5\x90\xaf\xe7\x94\xa8')),
            ],
            options={
                'verbose_name': '\u5730\u5740',
                'verbose_name_plural': '\u5730\u5740',
            },
            bases=(models.Model,),
        ),
    ]
