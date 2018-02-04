from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.views.generic import (
	TemplateView,
	ListView,
	DetailView
)
from .models import Country

class HomeView(TemplateView):
	template_name='countries/home.html'
	#def get(self, request, *args, **kwargs):
		#return render(request,"countries/home.html")

class CountryDetailView(TemplateView):
	template_name='countries/country_detail.html'

	def get_context_data(self, *args, **kwargs):
		code = kwargs['code']
		return {'code':code}

class CountryDetailIdView(DetailView):
	template_name='countries/country_id_detail.html'

	#Mismo funcionamiento con una vista que ya se encarga de ellos
	model = Country

	#def get_context_data(self, *args, **kwargs):
		#Manera manual con get_object_or_404
		#country = get_object_or_404(Country,id=kwargs['id'])
		#Manera aun mas manual usando un try cath y lanzando Http404

		#return {'country':country}

class TagsView(TemplateView):
	template_name='countries/tags.html'

class CountrySearchView(ListView):
	template_name='countries/search.html'
	#model = Country

	def get_queryset(self):
		query = self.kwargs['query']
		return Country.objects.filter(name__contains=query)

	# def get_context_data(self, *args, **kwargs):

	# 	colombia = {'name': 'colombia', 'code':'CO'}
	# 	usa = {'name':'estados unidos','code':'USA'}
	# 	mexico = {'name':'Mexico','code':'MX'}

	# 	countries = [colombia,usa,mexico]
	# 	return {'countries' : countries}
