from django.views import View
from ..models import Zone
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
class ZoneView:
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request,id = 0):
        if(id>0):
            corregimientos= list(Zone.objects.filter(id=id).values())
            if len(corregimientos) >0:
                dates = {'message':'Success','corregimiento': corregimientos}
            else:
                dates = {'message':'Corregimiento not found...'}
            return JsonResponse(dates)
        else:
            corregimientos = list(Zone.objects.values())
            if len(corregimientos)>0:
                dates = {'message':'Success','corregimeinto': corregimientos}
            else:
                dates = {'message':'Corregimiento not found...'}
            return JsonResponse(dates)
        
    def post(self,request):
        jd = json.loads(request.body)
        Zone.objects.create(description=jd['description'],city_id_id=jd['city_id'])
        dates = {'message':'Success'}
        return JsonResponse(dates)


    def put(self,request,id):
        jd = json.loads(request.body)
        corregimientos =list(Zone.objects.filter(id=id).values())
        if len(corregimientos)>0:
            corregimientos = Zone.objects.get(id = id)
            corregimientos.description=jd['description']
            corregimientos.city_id=jd['city_id']
            corregimientos.save()
            dates ={'message':'Success'}
            
        else:
            dates = {'message':'Corregimiento not found...'}
        return JsonResponse(dates)

    def delete(self,request,id):
        corregimientos =list(Zone.objects.filter(id=id).values())
        if len(corregimientos)>0:
            Zone.objects.filter(id=id).delete()
            dates ={'message':'Success'}
        else:
            dates = {'message':'Corregimiento not found...'}
        return JsonResponse(dates)