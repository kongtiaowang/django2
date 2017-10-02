# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from courses.models import Course
from courses.models import Step
# Register your models here.

class StepInline(admin.StackedInline):
	model = Step

class CourseAdmin(admin.ModelAdmin):
	inlines = [StepInline,]	




admin.site.register(Course,CourseAdmin)
#admin.site.register(Step)