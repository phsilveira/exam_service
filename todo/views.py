# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

# Django
from django.shortcuts import render
from django.contrib.auth.models import User

# REST framework
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

# Provider OAuth2
# from provider.oauth2.models import Client

# Todo App
from todo.serializers import RegistrationSerializer, UserSerializer, TodoSerializer, AnswerKeySerializer
from todo.models import Todo, AnswerKey, Answer

class RegistrationView(APIView):
	""" Allow registration of new users """
	permission_classes = ()

	def post(self, request):
		serializer = RegistrationSerializer(data=request.data)

		# Check format and unique constraint
		if not serializer.is_valid():
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

		data = serializer.data

		u = User.objects.create(username=data['username'])
		u.set_password(data['password'])
		u.save()

		# Create OAuth2 client
		# name = u.username
		# client = Client(user=u, name=name, url='' + name, client_id=name, client_secret='', client_type=1)
		# client = save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)


class TodosView(APIView):
	permission_classes = (
		# IsAuthenticated, 
		)

	def get(self, request):
		""" Get all todos """
		# todos = Todo.objects.filter(owner=request.user.id)
		todos = Todo.objects.all()
		serializer = TodoSerializer(todos, many=True)
		return Response(serializer.data)

	def post(self, request):
		""" Adding a new todo """
		serializer = TodoSerializer(data=request.data)
		if not serializer.is_valid():
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

		else:
			data = request.data
			# owner = request.user
			owner = User.objects.first()
			t = Todo.objects.create(owner=owner, description=data['description'], done=False)
			t.save()
			# data['id'] = t.pk
			return Response(request.data, status=status.HTTP_201_CREATED)

	def put(self, request):
		""" Update a todo """
		serializer = TodoSerializer(data=request.data)
		if not serializer.is_valid():
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

		else:
			data = serializer.data
			desc = data['description']
			done = data['done']
			t = Todo(id=todo_id, owner=request.user, description=desc, done=done, update=datetime.now())
			t.save()
			return Response(status=status.HTTP_200_OK)

class AnswerKeyView(APIView):
	permission_classes = ()

	def get(self, request):
		answers = AnswerKey.objects.all()
		serializer = AnswerKeySerializer(answers, many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer = AnswerKeySerializer(data=request.data)
		if not serializer.is_valid():
			return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)
		else:
			data = serializer.data
			answer_key = AnswerKey.objects.create(student_id=data['student_id'],
													student_name=data['student_name'],
													exam=data['exam'],
													version=data['version'],
													discipline=data['discipline'])
			answer_key.save()

			print data

			for answer in data['answers']:
				a = Answer.objects.create(answer_key=answer_key,
											value=answer['value'])
				print answer['value']

			return Response(request.data, status=status.HTTP_201_CREATED)
