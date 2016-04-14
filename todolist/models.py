from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User, Group
from rest_framework import serializers

class Todo(models.Model):
    task = models.CharField(max_length=100, unique = True)
    completed = models.BooleanField(default = False) 
    def __str__(self):
        return self.task
	class Meta:
	    ordering = ['task']
				
