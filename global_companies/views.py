# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def myView(request):
# 	return HttpResponse("Hello, World!")

def viewHomePage(request):
	return render(request, 'homepage.html')

def viewSearchPage(request):
	return render(request, 'searchpage.html')

def search(request):
	search_query = ""
	if(request.method == 'GET'):
		search_query = request.GET.get('search_box', None)
	return HttpResponse(search_query)