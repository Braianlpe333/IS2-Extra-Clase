from django.urls import path
from .views.CityView import CityView
from .views.PublicationView import PublicationView
from .views.ZoneView import ZoneView
from django.views import generic
from .views.PublicationTypeView import PublicationTypeView
urlpatterns = [
    path('citys/',CityView.as_view(), name='city_list'),
    path('citys/<int:id>',CityView.as_view(), name='city_process'),
    path('publication/', PublicationView.as_view(), name='Publication_list'),
    path('publication/<int:id>',PublicationView.as_view(), name='Publication_process'),
    path('zone/', ZoneView.as_view(), name='Zone_list'),
    path('zone/<int:id>',ZoneView.as_view(), name='Zone_process'),
    path('publicationtype/', PublicationTypeView.as_view(), name='publicationtype_list'),
    path('publicationtype/<int:id>',PublicationTypeView.as_view(), name='publicationtype_process'),
    path('view2/',
        generic.TemplateView.as_view(template_name='view2.html')),
    path('',
        generic.TemplateView.as_view(template_name='view1.html')),
]