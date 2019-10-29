# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
# def myView(request):
# 	return HttpResponse("Hello, World!")

def viewHomePage(request):
	return render(request, 'homepage.html')

def viewSearchPage(request):
	return render(request, 'searchpage.html')