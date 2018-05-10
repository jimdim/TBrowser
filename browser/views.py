from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return render(request, 'browser/home.html')

def profile(request):
	return render(request, 'browser/basic.html',{

		'pieces': ['This is where There will be a profile window'],

		})

def settings(request):
	return render(request, 'browser/basic.html',{

		'pieces': ['This is the settings page.', 'This is where the user can change some preferences such as themes.'],

		})
