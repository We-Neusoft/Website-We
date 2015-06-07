# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_uuid_pk.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', django_uuid_pk.fields.UUIDField(primary_key=True, serialize=False, editable=False, max_length=36, blank=True, unique=True)),
                ('name', models.CharField(max_length=32, verbose_name='\u5206\u7c7b')),
                ('order', models.IntegerField(verbose_name='\u6392\u5e8f')),
                ('parent', models.ForeignKey(verbose_name='\u4e0a\u7ea7\u5206\u7c7b', blank=True, to='genuine.Catalog', null=True)),
            ],
            options={
                'ordering': ['parent', 'order'],
                'verbose_name': '\u5206\u7c7b',
                'verbose_name_plural': '\u5206\u7c7b',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32, verbose_name='\u540d\u79f0')),
                ('order', models.IntegerField(verbose_name='\u6392\u5e8f')),
                ('file_id', models.CharField(max_length=22, verbose_name='\u6587\u4ef6ID')),
                ('parent', models.ForeignKey(verbose_name='\u4e0a\u7ea7\u5206\u7c7b', to='genuine.Catalog')),
            ],
            options={
                'ordering': ['parent', 'order'],
                'verbose_name': '\u6761\u76ee',
                'verbose_name_plural': '\u6761\u76ee',
            },
            bases=(models.Model,),
        ),
    ]
