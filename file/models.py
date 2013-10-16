#coding=utf-8
import uuid

from django.db import models

from django_uuid_pk.fields import UUIDField

class File(models.Model):
    id = UUIDField(primary_key=True)
    name = models.CharField('文件名', max_length=128)
    extension = models.CharField('扩展名', max_length=16)
    size = models.BigIntegerField('大小', editable=False)
    type = models.TextField('属性', editable=False)
    mime = models.CharField('MIME类型', max_length=64, editable=False)
    crc32 = models.CharField('CRC32值', max_length=8, editable=False)
    md5sum = models.CharField('MD5值', max_length=22, editable=False)
    sha1sum = models.CharField('SHA1值', max_length=27, editable=False)
    created = models.DateTimeField('上传时间', auto_now_add=True, editable=False)

    def __unicode__(self):
        return self.name

    class Meta:
        index_together = [
            ['md5sum', 'sha1sum'],
        ]
        ordering = ['-created']
        verbose_name = '文件'
        verbose_name_plural = '文件'
