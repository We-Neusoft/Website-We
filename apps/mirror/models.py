#coding=utf8
from django.db import models

class Mirror(models.Model):
    name = models.CharField(u'镜像名称', max_length=32)
    order = models.IntegerField(u'排序')
    description = models.TextField(u'描述', blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['order']
        verbose_name = u'镜像'
        verbose_name_plural = u'镜像'

class Status(models.Model):
    mirror = models.OneToOneField(Mirror, verbose_name=u'镜像名称')
    count = models.IntegerField(u'文件总数量', null=True, editable=False)
    size = models.BigIntegerField(u'文件总大小', null=True, editable=False)
    time = models.DateTimeField(u'上次成功同步时间', null=True, editable=False)
    status = models.SmallIntegerField(u'同步状态', null=True, editable=False)

    def __unicode__(self):
        return self.mirror.name

    class Meta:
        ordering = ['mirror']
        verbose_name = u'镜像状态'
        verbose_name_plural = u'镜像状态'
