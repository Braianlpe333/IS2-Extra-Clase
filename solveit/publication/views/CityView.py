from django.views import View
from ..models import City
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json


class CityView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request,id = 0):
        if(id>0):
            citys = list(City.objects.filter(id=id).values())
            if len(citys) >0:
                dates = {'message':'Success','citys': citys}
            else:
                dates = {'message':'City not found...'}
            return JsonResponse(dates)
        else:
            citys = list(City.objects.values())
            if len(citys)>0:
                dates = {'message':'Success','citys': citys}
            else:
                dates = {'message':'Citys not found...'}
            return JsonResponse(dates)
        
    def post(self,request):
        jd = json.loads(request.body)
        City.objects.create(description=jd['description'])
        dates = {'message':'Success'}
        return JsonResponse(dates)


    def put(self,request,id):
        jd = json.loads(request.body)
        citys =list(City.objects.filter(id=id).values())
        if len(citys)>0:
            citys = City.objects.get(id = id)
            citys.description=jd['description']
            citys.save()
            dates ={'message':'Success'}
            
        else:
            dates = {'message':'City not found...'}
        return JsonResponse(dates)

    def delete(self,request,id):
        citys =list(City.objects.filter(id=id).values())
        if len(citys)>0:
            City.objects.filter(id=id).delete()
            dates ={'message':'Success'}
        else:
            dates = {'message':'City not found...'}
        return JsonResponse(dates)