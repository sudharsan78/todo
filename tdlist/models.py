from __future__ import unicode_literals

from django.db import models

class Wrk(models.Model):
    wrk_lst=models.CharField(max_length=100)
    def __str__(self):
        return self.wrk_lst
