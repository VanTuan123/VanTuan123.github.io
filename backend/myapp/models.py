from django.db import models

class CRCInfo(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    data = models.TextField(default='')
