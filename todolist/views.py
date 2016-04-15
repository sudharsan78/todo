
from todolist.models import Todo
from todolist.serializers import TodoSerializer
from rest_framework import generics


class index(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer



