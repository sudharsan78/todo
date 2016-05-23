from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=owner)

class Todo(models.Model):
    task = models.CharField(max_length=100, unique = True, blank = False)
    completed = models.BooleanField(default = False) 
    owner = models.ForeignKey('auth.User', related_name='tasklist')
    def __str__(self):
        return self.task
        class Meta:
	    ordering = ['task']



		
		
    
   	
