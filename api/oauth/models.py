#coding=utf-8
from django.contrib.auth.models import User
from django.db import models

class RedirectionUri(models.Model):
    client = models.ForeignKey(User, verbose_name='应用端')
    uri = models.URLField('地址')

    class Meta:
        verbose_name = '跳转地址'
        verbose_name_plural = '跳转地址'
