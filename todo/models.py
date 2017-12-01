# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
	owner 		= models.ForeignKey(User)
	description = models.CharField(max_length=30)
	done 		= models.BooleanField()
	updated 	= models.DateTimeField(auto_now_add=True)

class OfficialAnswerKey(models.Model):
	exam 			= models.IntegerField()
	version 		= models.IntegerField()
	discipline 		= models.IntegerField()

class AnswerKey(models.Model):
	official_answer_key = models.ForeignKey(OfficialAnswerKey,on_delete=models.PROTECT, null=True)
	student_id 		= models.IntegerField()
	student_name 	= models.CharField(max_length=200)
	exam 			= models.IntegerField()
	version 		= models.IntegerField()
	discipline 		= models.IntegerField()

	def __str__(self):
		return u"%s" % self.student_name

class Answer(models.Model):
	answer_key = models.ForeignKey(AnswerKey,related_name='answers', on_delete=models.CASCADE)
	key = models.IntegerField()
	value = models.IntegerField()

