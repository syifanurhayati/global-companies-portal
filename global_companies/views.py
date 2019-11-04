# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def viewHomePage(request):
	return render(request, 'homepage.html')

def viewSearchPage(request):
	search_query = ""
	if(request.method == 'GET'):
		search_query = request.GET.get('search_box', None)
	print(search_query)
	# return render(request, 'searchpage.html', search_query)
	return HttpResponse('<h1>This query is {}.</h1>'.format(search_query));