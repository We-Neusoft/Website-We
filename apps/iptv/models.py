#coding=utf8
from django.db import models

from django_uuid_pk.fields import UUIDField

class Group(models.Model):
    name = models.CharField(u'频道组', max_length=32)
    order = models.IntegerField(u'排序')

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['order']
        verbose_name = u'频道组'
        verbose_name_plural = u'频道组'

class Channel(models.Model):
    group = models.ForeignKey(Group, verbose_name=u'频道组')
    name = models.CharField(u'频道名', max_length=32)
    channel = models.CharField(u'频道号', max_length=32)
    order = models.IntegerField(u'排序')

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['group', 'order']
        verbose_name = u'频道'
        verbose_name_plural = u'频道'

class Point(models.Model):
    id = UUIDField(primary_key=True)
    channel = models.ForeignKey(Channel, verbose_name=u'频道')
    source = models.CharField(u'源名称', max_length=32)
    target = models.CharField(u'目标名', max_length=32)
    hd = models.BooleanField(u'高清', default=False)
    sound = models.IntegerField(u'声道数')
    active = models.BooleanField(u'活动', default=False)

    def __unicode__(self):
        return self.channel.name

    class Meta:
        ordering = ['channel', '-hd']
        verbose_name = u'频道点'
        verbose_name_plural = u'频道点'

class Guide(models.Model):
    channel = models.ForeignKey(Channel, verbose_name=u'频道')
    time = models.TimeField(u'时间')
    name = models.CharField(u'节目', max_length=64)

    def __unicode__(self):
        return self.channel.name + ' (' + str(self.time) + ')'

    class Meta:
        ordering = ['channel', 'time']
        verbose_name = u'节目'
        verbose_name_plural = u'节目'
