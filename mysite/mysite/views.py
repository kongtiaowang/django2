# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
	home_data = "This is a my home page!"
	return render(request, "home.html", {'home_data' : home_data})