#coding=utf-8
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

from django_uuid_pk.fields import UUIDField

from converter import file_size

class File(models.Model):
    id = UUIDField(primary_key=True)
    name = models.CharField(u'文件名', max_length=128)
    extension = models.CharField(u'扩展名', max_length=16)
    size = models.BigIntegerField(u'大小', editable=False)
    type = models.TextField(u'属性', editable=False)
    mime = models.CharField(u'MIME类型', max_length=64, editable=False)
    crc32 = models.CharField(u'CRC32值', max_length=8, editable=False)
    md5sum = models.CharField(u'MD5值', max_length=22, editable=False)
    sha1sum = models.CharField(u'SHA1值', max_length=27, editable=False)
    created = models.DateTimeField(u'上传时间', auto_now_add=True, editable=False)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('file:detail', args=[urlsafe_base64_encode(self.id.bytes)])

    def size_unit(self):
        return file_size(self.size)

    def md5(self):
        return self.decode(self.md5sum)

    def sha1(self):
        return self.decode(self.sha1sum)

    def decode(self, encoded):
        return urlsafe_base64_decode(encoded).encode('hex')

    def download_times(self):
        return self.download_set.order_by('file', 'ip', 'time').distinct('file', 'ip', 'time').count()

    class Meta:
        index_together = [
            ['md5sum', 'sha1sum'],
        ]
        ordering = ['-created']
        verbose_name = u'文件'
        verbose_name_plural = u'文件'

class Download(models.Model):
    file = models.ForeignKey('File', verbose_name='文件', editable=False)
    ip = models.GenericIPAddressField(u'用户IP', editable=False)
    referer = models.URLField(u'访问来源', null=True, editable=False)
    time = models.DateTimeField(u'下载时间', editable=False)

    def __unicode__(self):
        return self.file.name

    class Meta:
        unique_together = [
            ['file', 'ip', 'time'],
        ]
        ordering = ['-time']
        verbose_name = u'下载记录'
        verbose_name_plural = u'下载记录'
