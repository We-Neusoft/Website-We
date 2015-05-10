#coding=utf8
from django.db import models

from django_uuid_pk.fields import UUIDField

class NavbarItem(models.Model):
    id = UUIDField(primary_key=True)
    key = models.CharField('标识', max_length=16, unique=True)
    order = models.IntegerField('排序')
    title = models.CharField('标题', max_length=64)
    intranet = models.BooleanField('校园网', default=False)
    internet = models.BooleanField('互联网', default=False)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['order', 'key']
        verbose_name = '导航项'
        verbose_name_plural = '导航项'

class NavbarMore(models.Model):
    id = UUIDField(primary_key=True)
    app = models.ForeignKey(NavbarItem)
    key = models.CharField('标识', max_length=16)
    order = models.IntegerField('排序')
    title = models.CharField('标题', max_length=64)
    subtitle = models.CharField('副标题', max_length=64)
    content = models.TextField('正文')
    intranet = models.BooleanField('校园网', default=False)
    internet = models.BooleanField('互联网', default=False)
    modified = models.DateTimeField('最后修改', auto_now=True)

    def __unicode__(self):
        return self.title

    class Meta:
        unique_together = ('app', 'key')
        ordering = ['app', 'order', 'key']
        verbose_name = '导航更多'
        verbose_name_plural = '导航更多'
