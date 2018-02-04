from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

class HomeView(TemplateView):
	template_name='countries/home.html'
	#def get(self, request, *args, **kwargs):
		#return render(request,"countries/home.html")


class TagsView(TemplateView):
	template_name='countries/tags.html'

	# def get_context_data(self, *args, **kwargs):

	# 	colombia = {'name': 'colombia', 'code':'CO'}
	# 	usa = {'name':'estados unidos','code':'USA'}
	# 	mexico = {'name':'Mexico','code':'MX'}

	# 	countries = [colombia,usa,mexico]
	# 	return {'countries' : countries}
