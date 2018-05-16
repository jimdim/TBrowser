from django.shortcuts import render
from django.http import HttpResponse

from django.views import generic
from .models import Dashboard

class IndexView(generic.ListView):
	template_name = 'browser/home.html'

	def get_queryset(self):

		dash_list = Dashboard.objects.all().order_by("id")
		
		i = 0

		row1 = [];	row2 = []; row3 = []; row4 = []; row5 = [];
		
		for item in dash_list:
			if i < 6:
				row1.append(dash_list[i])
			elif i < 12:
				row2.append(dash_list[i])
			elif i < 18:
				row3.append(dash_list[i])
			elif i < 24:
				row4.append(dash_list[i])
			elif i < 30:
				row5.append(dash_list[i])
			i+=1

		return [row1,row2,row3,row4,row5]


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
