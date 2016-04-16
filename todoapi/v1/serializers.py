from rest_framework import serializers
from todoapi.models import TodoAPI


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoAPI
        fields = ('task', 'completed')
