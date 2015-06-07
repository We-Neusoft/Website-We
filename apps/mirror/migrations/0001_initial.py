# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mirror',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32, verbose_name='\u955c\u50cf\u540d\u79f0')),
                ('order', models.IntegerField(verbose_name='\u6392\u5e8f')),
                ('description', models.TextField(verbose_name='\u63cf\u8ff0', blank=True)),
                ('active', models.BooleanField(default=False, verbose_name='\u6d3b\u52a8')),
            ],
            options={
                'ordering': ['order'],
                'verbose_name': '\u955c\u50cf',
                'verbose_name_plural': '\u955c\u50cf',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('count', models.IntegerField(verbose_name='\u6587\u4ef6\u603b\u6570\u91cf', null=True, editable=False)),
                ('size', models.BigIntegerField(verbose_name='\u6587\u4ef6\u603b\u5927\u5c0f', null=True, editable=False)),
                ('time', models.DateTimeField(verbose_name='\u4e0a\u6b21\u6210\u529f\u540c\u6b65\u65f6\u95f4', null=True, editable=False)),
                ('status', models.SmallIntegerField(verbose_name='\u540c\u6b65\u72b6\u6001', null=True, editable=False)),
                ('mirror', models.OneToOneField(verbose_name='\u955c\u50cf\u540d\u79f0', to='mirror.Mirror')),
            ],
            options={
                'ordering': ['mirror'],
                'verbose_name': '\u955c\u50cf\u72b6\u6001',
                'verbose_name_plural': '\u955c\u50cf\u72b6\u6001',
            },
            bases=(models.Model,),
        ),
    ]
