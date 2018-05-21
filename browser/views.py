from django.shortcuts import render
from django.http import HttpResponse

from django.views import generic
from .models import Dashboard, UserMatchedCategory, PinnedDashboard

class IndexView(generic.ListView):
	template_name = 'browser/home.html'

	def get_queryset(self):

		cur_user = 'adam'

		interest_list = UserMatchedCategory.objects.filter(usernameUMC_id=cur_user).order_by("scoreUMC")

		pinned_list = Dashboard.objects.filter(pinneddashboard__usernamePD_id=cur_user)

		cat_row2 = interest_list[0].categoryUMC_id
		cat_row3 = interest_list[1].categoryUMC_id
		cat_row4 = interest_list[2].categoryUMC_id
		cat_row5 = interest_list[3].categoryUMC_id

		r2_dash_list = Dashboard.objects.filter(dashmatchedcategory__categoryDMC=cat_row2).order_by("dashmatchedcategory__scoreDMC")
		r3_dash_list = Dashboard.objects.filter(dashmatchedcategory__categoryDMC=cat_row3).order_by("dashmatchedcategory__scoreDMC")
		r4_dash_list = Dashboard.objects.filter(dashmatchedcategory__categoryDMC=cat_row4).order_by("dashmatchedcategory__scoreDMC")
		r5_dash_list = Dashboard.objects.filter(dashmatchedcategory__categoryDMC=cat_row5).order_by("dashmatchedcategory__scoreDMC")

		row1 = [];	row2 = []; row3 = []; row4 = []; row5 = []; i = 0

		if len(pinned_list) > 0:

			for item in pinned_list:
				row1.append(pinned_list[i])
				i+=1

			i = 6

			for item in range(24):
				if i < 12:
					if len(r2_dash_list) > i-6:
						row2.append(r2_dash_list[i-6])
				elif i < 18:
					if len(r3_dash_list) > i-12:
						row3.append(r3_dash_list[i-12])
				elif i < 24:
					if len(r4_dash_list) > i-18:
						row4.append(r4_dash_list[i-18])
				elif i < 30:
					if len(r5_dash_list) > i-24:
						row5.append(r5_dash_list[i-24])
				i+=1

		else:
			
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

		rows_list = [row1,row2,row3,row4,row5]	

		return rows_list		

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
