# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Course(models.Model):
	"""docstring for ClassName"""
	create_at = models.DateTimeField(auto_now_add = True)
	title = models.CharField(max_length=255)
	description = models.TextField()

	def __str__(self):
		return self.title


class Step(models.Model):
	"""docstring for ClassName"""
	title = models.CharField(max_length=255)
	description = models.TextField()
	order = models.IntegerField(default=0)
	course = models.ForeignKey(Course)

	class Meta:
		unique_together = ('course', 'title')

	def __str__(self):
		return self.title

