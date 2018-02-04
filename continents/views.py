from django.shortcuts import render
from django.views.generic import TemplateView


class ContinentsView(TemplateView):
	template_name="continents/home.html"

	def get_context_data(self, *args, **kwargs):

		europa = {
			'name':'europa',
			'translate':'europe',
			'color':'#AE4'
		}

		asia = {
			'name':'asia',
			'translate':'asia',
			'color':'#F33'
		}


		america = {
			'name':'america',
			'translate':'america',
			'color':'#D22'
		}


		africa = {
			'name':'africa',
			'translate':'africa',
			'color':'#34D'
		}


		antartica  = {
			'name':'antartica',
			'translate':'antarctica',
			'color':'#385'
		}

		australia  = {
			'name':'australia',
			'translate':'australia',
			'color':'#DEA'
		}

		continents = [europa,asia,america,africa,antartica,australia]
		return {'continents':continents}

