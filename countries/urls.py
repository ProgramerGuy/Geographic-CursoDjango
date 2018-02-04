from django.contrib import admin
from django.urls import path
from countries.views import (
	CountryDetailView,
	CountryDetailIdView,
	HomeView,
	CountrySearchView
)

urlpatterns = [
    path("search/<query>/", CountrySearchView.as_view(), name='country_search'),
    path("<int:pk>/", CountryDetailIdView.as_view(), name='country_id_detail'),
    path("<code>/", CountryDetailView.as_view(),name='country_code_detail')

]