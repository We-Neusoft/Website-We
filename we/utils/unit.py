#coding=utf-8

# 计算文件大小，使用相应的单位
def file_size(num):
   for x in ['Bytes', 'KB', 'MB', 'GB', 'TB', 'PB']:
      if num < 1024.0:
         return '%3.2f %s' % (num, x)
      num /= 1024.0