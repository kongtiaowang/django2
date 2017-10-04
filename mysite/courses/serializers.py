from rest_framework import serializers
from . import models

class CourseSerializer(serializers.ModelSerializer):
	class Meta:
		fields = (
			'create_at',
			'title',
			'description',
		)
		model = models.Course


class StepSerializer(serializers.ModelSerializer):
	class Meta:
		fields = (
			'description',
			'title',
			'order',
			'course'
		)
		model = models.Step