
from todoapi.models import TodoAPI
from todoapi.serializers import TodoSerializer
from rest_framework import generics


class TodoAPIView(generics.ListCreateAPIView):
    queryset = TodoAPI.objects.all()
    serializer_class = TodoSerializer
