# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from rest_framework import viewsets
from .models import Course
from .models import Step
from .forms import CourseForm
from courses.serializers import CourseSerializer,StepSerializer
# Create your views here.

def get_courses(request):
	courses = Course.objects.all()
	return render(request, 'courses/get_courses.html', {'courses':courses})

def course_detail(request, pk):
	# course = Course.objects.get(pk=pk)
	course = get_object_or_404(Course,pk=pk)
	return render(request, 'courses/course_detail.html', {'course':course})

def step_detail(request, course_pk, step_pk):
	# course = Course.objects.get(pk=pk)
	step = get_object_or_404(Step, course_id=course_pk, pk=step_pk)
	return render(request, 'courses/step_detail.html', {'step': step})

def courses_add(request):
	form = CourseForm()
	if request.method == 'POST':
		form = CourseForm(request.POST)
		if form.is_valid():
			course = form.save(commit=False)
			course.save()
			return HttpResponseRedirect("/")
	return render(request, 'courses/course_add.html',{'form': form})

class CourseViewSet(viewsets.ModelViewSet):
	queryset = Course.objects.all()
 	serializer_class = CourseSerializer

class StepViewSet(viewsets.ModelViewSet):
	queryset = Step.objects.all()
 	serializer_class = StepSerializer

 		