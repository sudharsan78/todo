from __future__ import unicode_literals

from django.db import models

class Todo(models.Model):
    work_list=models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.work_list
	class Meta:
	    ordering=['work_list']
				
