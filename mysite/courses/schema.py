from graphene_django import DjangoObjectType
from graphene.types.objecttype import ObjectType
from . import models

import graphene

class CourseType(DjangoObjectType):
	class Meta:
		model = models.Course

class StepType(DjangoObjectType):
	class Meta:
		model = models.Step

class Query(graphene.ObjectType):
	all_courses = graphene.List(CourseType)
	all_steps = graphene.List(StepType)

	course = graphene.Field(CourseType,id=graphene.Int(),title=graphene.String())
	step = graphene.Field(StepType,id=graphene.Int(),title=graphene.String())

	def resolve_all_courses(self, info, **kwargs):
		return models.Course.objects.all()

	def resolve_all_steps(self, info, **kwargs):
		return models.Step.objects.all()

	def resolve_course(self, info, **kwargs):
		id = kwargs.get('id')
		title = kwargs.get('title')

		if id is not None:
			return models.Course.objects.get(pk=id)

		if title is not None:
			return models.Course.objects.get(title=title)

		return None
	def resolve_step(self, info, **kwargs):
		id = kwargs.get('id')
		title = kwargs.get('title')

		if id is not None:
			return models.Step.objects.get(pk=id)

		if title is not None:
			return models.Step.objects.get(title=title)

		return None