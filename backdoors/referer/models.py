from django.db import models

class Url(models.Model):
    url = models.URLField('URL')
