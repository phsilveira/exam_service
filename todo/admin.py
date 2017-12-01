# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from todo.models import Todo, AnswerKey, Answer

admin.site.register(Todo)

class AnswerOption(admin.StackedInline):
	model = Answer

class AnswerKeyAdmin(admin.ModelAdmin):
	inlines = [AnswerOption,]

admin.site.register(AnswerKey, AnswerKeyAdmin)
