# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_uuid_pk.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Download',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip', models.GenericIPAddressField(verbose_name='\u7528\u6237IP', editable=False)),
                ('referer', models.URLField(verbose_name='\u8bbf\u95ee\u6765\u6e90', null=True, editable=False)),
                ('time', models.DateTimeField(verbose_name='\u4e0b\u8f7d\u65f6\u95f4', editable=False)),
            ],
            options={
                'ordering': ['-time'],
                'verbose_name': '\u4e0b\u8f7d\u8bb0\u5f55',
                'verbose_name_plural': '\u4e0b\u8f7d\u8bb0\u5f55',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', django_uuid_pk.fields.UUIDField(primary_key=True, serialize=False, editable=False, max_length=36, blank=True, unique=True)),
                ('name', models.CharField(max_length=128, verbose_name='\u6587\u4ef6\u540d')),
                ('extension', models.CharField(max_length=16, verbose_name='\u6269\u5c55\u540d')),
                ('size', models.BigIntegerField(verbose_name='\u5927\u5c0f', editable=False)),
                ('type', models.TextField(verbose_name='\u5c5e\u6027', editable=False)),
                ('mime', models.CharField(verbose_name='MIME\u7c7b\u578b', max_length=64, editable=False)),
                ('crc32', models.CharField(verbose_name='CRC32\u503c', max_length=8, editable=False)),
                ('md5sum', models.CharField(verbose_name='MD5\u503c', max_length=22, editable=False)),
                ('sha1sum', models.CharField(verbose_name='SHA1\u503c', max_length=27, editable=False)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='\u4e0a\u4f20\u65f6\u95f4')),
            ],
            options={
                'ordering': ['-created'],
                'verbose_name': '\u6587\u4ef6',
                'verbose_name_plural': '\u6587\u4ef6',
            },
            bases=(models.Model,),
        ),
        migrations.AlterIndexTogether(
            name='file',
            index_together=set([('md5sum', 'sha1sum')]),
        ),
        migrations.AddField(
            model_name='download',
            name='file',
            field=models.ForeignKey(editable=False, to='file.File', verbose_name=b'\xe6\x96\x87\xe4\xbb\xb6'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='download',
            unique_together=set([('file', 'ip', 'time')]),
        ),
    ]
