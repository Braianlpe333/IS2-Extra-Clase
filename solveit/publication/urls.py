from django.urls import path
from .views.CityView import CityView
from .views.PublicationView import PublicationView
from django.views import generic
urlpatterns = [
    path('citys/',CityView.as_view(), name='city_list'),
    path('citys/<int:id>',CityView.as_view(), name='city_process'),
    path('publication/', PublicationView.as_view(), name='Publication_list'),
    path('publication/<int:id>',PublicationView.as_view(), name='Publication_process'),
    path('view2/',
        generic.TemplateView.as_view(template_name='view2.html')),
    path('',
        generic.TemplateView.as_view(template_name='view1.html')),
]