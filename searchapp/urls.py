from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path(
        'african/countries/urban_areas/',
        views.GetAfricanCountries.as_view(),
        name='african-countries'),
    path(
        'african/countries/urban_area/<str:country>/',
        views.GetAfricanCountriesUrbanArea.as_view(),
        name='afircan-urban-area'),
]
