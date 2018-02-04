from django.shortcuts import render
from django.views.generic import(
	TemplateView,
	ListView,
	DetailView
)
from .models import Continent


class ContinentsView(ListView):
	template_name="continents/home.html"
	model = Continent

class ContinentDetailView(DetailView):
	template_name="continents/detail.html"
	model = Continent 
