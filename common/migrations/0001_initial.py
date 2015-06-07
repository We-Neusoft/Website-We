# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_uuid_pk.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NavbarItem',
            fields=[
                ('id', django_uuid_pk.fields.UUIDField(primary_key=True, serialize=False, editable=False, max_length=36, blank=True, unique=True)),
                ('key', models.CharField(unique=True, max_length=16, verbose_name=b'\xe6\xa0\x87\xe8\xaf\x86')),
                ('order', models.IntegerField(verbose_name=b'\xe6\x8e\x92\xe5\xba\x8f')),
                ('title', models.CharField(max_length=64, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
                ('intranet', models.BooleanField(default=False, verbose_name=b'\xe6\xa0\xa1\xe5\x9b\xad\xe7\xbd\x91')),
                ('internet', models.BooleanField(default=False, verbose_name=b'\xe4\xba\x92\xe8\x81\x94\xe7\xbd\x91')),
            ],
            options={
                'ordering': ['order', 'key'],
                'verbose_name': '\u5bfc\u822a\u9879',
                'verbose_name_plural': '\u5bfc\u822a\u9879',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NavbarMore',
            fields=[
                ('id', django_uuid_pk.fields.UUIDField(primary_key=True, serialize=False, editable=False, max_length=36, blank=True, unique=True)),
                ('key', models.CharField(max_length=16, verbose_name=b'\xe6\xa0\x87\xe8\xaf\x86')),
                ('order', models.IntegerField(verbose_name=b'\xe6\x8e\x92\xe5\xba\x8f')),
                ('title', models.CharField(max_length=64, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
                ('subtitle', models.CharField(max_length=64, verbose_name=b'\xe5\x89\xaf\xe6\xa0\x87\xe9\xa2\x98')),
                ('content', models.TextField(verbose_name=b'\xe6\xad\xa3\xe6\x96\x87')),
                ('intranet', models.BooleanField(default=False, verbose_name=b'\xe6\xa0\xa1\xe5\x9b\xad\xe7\xbd\x91')),
                ('internet', models.BooleanField(default=False, verbose_name=b'\xe4\xba\x92\xe8\x81\x94\xe7\xbd\x91')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9c\x80\xe5\x90\x8e\xe4\xbf\xae\xe6\x94\xb9')),
                ('app', models.ForeignKey(to='common.NavbarItem')),
            ],
            options={
                'ordering': ['app', 'order', 'key'],
                'verbose_name': '\u5bfc\u822a\u66f4\u591a',
                'verbose_name_plural': '\u5bfc\u822a\u66f4\u591a',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='navbarmore',
            unique_together=set([('app', 'key')]),
        ),
    ]
