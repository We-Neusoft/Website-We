#coding=utf-8
from django.db import models

# 更多服务
class MoreService(models.Model):
    key = models.CharField('标识', max_length=16)
    order = models.IntegerField('排序')
    title = models.CharField('标题', max_length=64)
    subtitle = models.CharField('副标题', max_length=64)
    content = models.TextField('正文')
    intranet = models.BooleanField('校园网')
    internet = models.BooleanField('互联网')
    modified = models.DateTimeField('最后修改', auto_now=True)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['order']
        verbose_name = '更多服务'
        verbose_name_plural = '更多服务'
