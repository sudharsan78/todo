from django.shortcuts import render

from .serializers import TodoSerializer
from rest_framework import generics

from todolist.models import Todo

from rest_framework import views


from rest_framework.views import APIView





class TodoAPIView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    def apiindex(request):
        return render(request, 'todolist/ab.html', queryset)

class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer