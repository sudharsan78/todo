from rest_framework import serializers
from todolist.models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        models = Todo
        fields = ('task', 'completed')
   

