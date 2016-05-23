from rest_framework import serializers
from todolist.models import Todo
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id','task', 'completed')


class UserSerializer(serializers.ModelSerializer):
    tasklist = serializers.PrimaryKeyRelatedField(many=True, queryset=Todo.objects.all())
    owner = serializers.ReadOnlyField(source='owner.username')
    # for username in User.objects.all():
    # 	Token.objects.get_or_create(user=username)
    class Meta:
        model = User
        fields = ('id', 'username', 'tasklist','owner')

# class TodoSerializer(serializers.HyperlinkedModelSerializer):
# 	owner = serializers.ReadOnlyField(source='owner.username')
# 	class Meta:
# 		model = Todo
# 		fields = ('url', 'owner', 'task', 'completed')


# class UserSerializer(serializers.ModelSerializer):
#     tasklist = serializers.HyperlinkedRelatedField(many=True, view_name='todo-detail', read_only=True)
#     class Meta:
#         model = User
#         fields = ('url', 'username', 'tasklist',)




