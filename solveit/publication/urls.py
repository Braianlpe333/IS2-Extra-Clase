from django.urls import path
from .views.CityView import *
urlpatterns = [
    path('citys/',CityView.as_view(), name='city_list'),
    path('citys/<int:id>',CityView.as_view(), name='companies_process')
]