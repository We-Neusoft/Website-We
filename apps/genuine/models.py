#coding=utf8
from django.db import models

from django_uuid_pk.fields import UUIDField

class Catalog(models.Model):
    id = UUIDField(primary_key=True)
    parent = models.ForeignKey('self', verbose_name=u'上级分类', null=True, blank=True)
    name = models.CharField(u'分类', max_length=32)
    order = models.IntegerField(u'排序')

    def __unicode__(self):
        if self.parent:
            return unicode(self.parent) + '/' + self.name
        else:
            return '/' + self.name

    class Meta:
        ordering = ['order']
        verbose_name = u'分类'
        verbose_name_plural = u'分类'

class Item(models.Model):
    parent = models.ForeignKey(Catalog, verbose_name=u'上级分类')
    name = models.CharField(u'名称', max_length=32)
    order = models.IntegerField(u'排序')
    file_id = models.CharField(u'文件ID', max_length=22)

    def __unicode__(self):
        return self.parent.name + '/' + self.name

    class Meta:
        ordering = ['parent', 'order']
        verbose_name = u'条目'
        verbose_name_plural = u'条目'