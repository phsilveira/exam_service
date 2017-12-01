from rest_framework import serializers
from todo.models import Todo, AnswerKey, Answer
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User

class RegistrationSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('username','password')

class TodoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Todo
		fields = ('id','description','done')

class AnswerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Answer
		fields = ('key','value',)

class AnswerKeySerializer(serializers.ModelSerializer):
	answers = AnswerSerializer(many=True,)
	class Meta:
		model = AnswerKey
		fields = ('student_id','student_name','exam','version','discipline','answers')