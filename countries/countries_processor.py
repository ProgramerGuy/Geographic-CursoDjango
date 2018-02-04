def countries_data(request):
	colombia = {'name': 'colombia', 'code':'CO'}
	usa = {'name':'estados unidos','code':'USA'}
	mexico = {'name':'Mexico','code':'MX'}

	countries = [colombia,usa,mexico]
	return {'countries' : countries}