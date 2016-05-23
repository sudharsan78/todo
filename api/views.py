from django.shortcuts import render

from .serializers import TodoSerializer, UserSerializer
from rest_framework import generics

from todolist.models import Todo

from rest_framework import views

from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework import filters
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from rest_framework import renderers
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class ExampleView(APIView):
    authentication_classes = (TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        content = {
            'user': unicode(request.user),  # `django.contrib.auth.User` instance.
            'auth': unicode(request.auth),  # None
        }
        return Response(content)

class TodoAPIView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    filter_backends = (filters.DjangoFilterBackend,filters.OrderingFilter,)
    filter_fields=('id',)
    ordering = ('-id',)
    def perform_create(self, serializer):
    	serializer.save(owner=self.request.user)
    	permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly,)

    # def apiindex(request):
    #     return render(request, 'todolist/ab.html', queryset)



class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly,)

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)



class UserTaskList(generics.ListAPIView):
    serializer_class = TodoSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering = ('-id',)
    def get_queryset(self):
        user = self.request.user.id
        return Todo.objects.filter(owner=user)


# @api_view(['GET'])
# def api_root(request, format=None):
#     return Response({
#         'users': reverse('user-list', request=request, format=format),
#         'tasklist': reverse('task-list', request=request, format=format)
#     })


# class SnippetHighlight(generics.GenericAPIView):
#     queryset = Todo.objects.all()
#     renderer_classes = (renderers.StaticHTMLRenderer,)

#     def get(self, request, *args, **kwargs):
#         snippet = self.get_object()
#         return Response(snippet)


