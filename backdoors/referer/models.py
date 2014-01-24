#coding=utf-8
from django.db import models

class Url(models.Model):
    url = models.URLField('URL')
    enable = models.BooleanField('启用')

    class Meta:
        verbose_name = '地址'
        verbose_name_plural = '地址'
