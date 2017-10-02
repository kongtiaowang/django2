# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from .models import Course
from .models import Step
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