from django.urls import path
from .views.CityView import CityView
from .views.PublicationView import PublicationView
urlpatterns = [
    path('citys/',CityView.as_view(), name='city_list'),
    path('citys/<int:id>',CityView.as_view(), name='city_process'),
    path('publication/', PublicationView.as_view(), name='Publication_list'),
    path('publication/<int:id>',PublicationView.as_view(), name='Publication_process'),
]