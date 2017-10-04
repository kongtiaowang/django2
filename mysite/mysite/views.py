# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from . import forms
import requests
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.

def home(request):
	return render(request, "home.html")


def suggestion(request):
	form = forms.SuggestionForm()
	url = 'http://www.github.com'
	if request.method == 'POST':
		cars = request.POST
		print(cars)
		return HttpResponseRedirect("/");

	return render(request, 'suggestion_form.html', {'form': form})

