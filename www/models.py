from django.db import models

# Create your models here.
class MoreService(models.Model):
    key = models.CharField(max_length=16)
    order = models.IntegerField()
    title = models.CharField(max_length=64)
    subtitle = models.CharField(max_length=64)
    content = models.TextField()
    modified = models.DateTimeField(auto_now=True)
