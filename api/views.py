from django.shortcuts import render

from .serializers import TodoSerializer
from rest_framework import generics

from todolist.models import Todo

from rest_framework import views


from rest_framework.views import APIView
from rest_framework import filters





class TodoAPIView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    filter_backends = (filters.DjangoFilterBackend,filters.OrderingFilter,)
    filter_fields=('id',)
    ordering = ('-id',)
    def apiindex(request):
        return render(request, 'todolist/ab.html', queryset)

class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
