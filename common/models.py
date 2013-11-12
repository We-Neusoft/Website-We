#coding=utf8
from django.db import models

from django_uuid_pk.fields import UUIDField

class NavbarItem(models.Model):
    id = UUIDField(primary_key=True)
    key = models.CharField('标识', max_length=16, unique=True)
    order = models.IntegerField('排序')
    title = models.CharField('标题', max_length=64)
    intranet = models.BooleanField('校园网')
    internet = models.BooleanField('互联网')

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['order', 'key']
        verbose_name = '导航项'
        verbose_name_plural = '导航项'
