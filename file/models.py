#coding=utf-8
import uuid

from django.db import models

from django_uuid_pk.fields import UUIDField

from we.utils.unit import file_size

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

    def size_unit(self):
        return file_size(self.size)

    def md5(self):
        return self.decode(self.md5sum)

    def sha1(self):
        return self.decode(self.sha1sum)

    def decode(self, encoded):
        encoded = encoded.replace('_', '/').replace('-', '+')
        if len(encoded) == 22:
            encoded += '=='
        elif len(encoded) == 27:
            encoded += '='

        return encoded.decode('base64').encode('hex')

    def download_times(self):
        return self.download_set.count()

    class Meta:
        index_together = [
            ['md5sum', 'sha1sum'],
        ]
        ordering = ['-created']
        verbose_name = '文件'
        verbose_name_plural = '文件'

class Download(models.Model):
    file = models.ForeignKey('File', verbose_name='文件', editable=False)
    ip = models.GenericIPAddressField('用户IP', editable=False)
    referer = models.URLField('访问来源', null=True, editable=False)
    time = models.DateTimeField('下载时间', auto_now_add=True, editable=False)

    def __unicode__(self):
        return self.file.name

    class Meta:
        ordering = ['-time']
        verbose_name = '下载记录'
        verbose_name_plural = '下载记录'
