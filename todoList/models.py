from django.db import models
from django import forms

models.Field.default = False

# Create your models here.
class TodoList(models.Model):
	title = models.CharField(max_length=20, unique=True)

	def __unicode__(self):
                return self.title

class TodoItem(models.Model):
	todoList = models.ForeignKey(TodoList)
	title = models.CharField(max_length=20, unique=True)
	description = models.TextField()
	isComplete = models.BooleanField()

	def __unicode__(self):
		return self.title
