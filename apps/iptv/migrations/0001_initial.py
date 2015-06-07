# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_uuid_pk.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32, verbose_name='\u9891\u9053\u540d')),
                ('channel', models.CharField(max_length=32, verbose_name='\u9891\u9053\u53f7')),
                ('order', models.IntegerField(verbose_name='\u6392\u5e8f')),
            ],
            options={
                'ordering': ['group', 'order'],
                'verbose_name': '\u9891\u9053',
                'verbose_name_plural': '\u9891\u9053',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32, verbose_name='\u9891\u9053\u7ec4')),
                ('order', models.IntegerField(verbose_name='\u6392\u5e8f')),
            ],
            options={
                'ordering': ['order'],
                'verbose_name': '\u9891\u9053\u7ec4',
                'verbose_name_plural': '\u9891\u9053\u7ec4',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Guide',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.TimeField(verbose_name='\u65f6\u95f4')),
                ('name', models.CharField(max_length=64, verbose_name='\u8282\u76ee')),
                ('channel', models.ForeignKey(verbose_name='\u9891\u9053', to='iptv.Channel')),
            ],
            options={
                'ordering': ['channel', 'time'],
                'verbose_name': '\u8282\u76ee',
                'verbose_name_plural': '\u8282\u76ee',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', django_uuid_pk.fields.UUIDField(primary_key=True, serialize=False, editable=False, max_length=36, blank=True, unique=True)),
                ('source', models.CharField(max_length=32, verbose_name='\u6e90\u540d\u79f0')),
                ('target', models.CharField(max_length=32, verbose_name='\u76ee\u6807\u540d')),
                ('hd', models.BooleanField(default=False, verbose_name='\u9ad8\u6e05')),
                ('active', models.BooleanField(default=False, verbose_name='\u6d3b\u52a8')),
                ('channel', models.ForeignKey(verbose_name='\u9891\u9053', to='iptv.Channel')),
            ],
            options={
                'ordering': ['channel', '-hd'],
                'verbose_name': '\u9891\u9053\u70b9',
                'verbose_name_plural': '\u9891\u9053\u70b9',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='channel',
            name='group',
            field=models.ForeignKey(verbose_name='\u9891\u9053\u7ec4', to='iptv.Group'),
            preserve_default=True,
        ),
    ]
