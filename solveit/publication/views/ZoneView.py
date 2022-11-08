from django.views import View
from ..models import Zone
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
class ZoneView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request,id = 0):
        if(id>0):
            zones= list(Zone.objects.filter(id=id).values())
            if len(zones) >0:
                dates = {'message':'Success','zones': zones}
            else:
                dates = {'message':'zones not found...'}
            return JsonResponse(dates)
        else:
            zones = list(Zone.objects.values())
            if len(zones)>0:
                dates = {'message':'Success','zones': zones}
            else:
                dates = {'message':'zones not found...'}
            return JsonResponse(dates)
        
    def post(self,request):
        jd = json.loads(request.body)
        Zone.objects.create(description=jd['description'],corregimiento=jd['corregimiento_id'])
        corregimeinto_id_id= jd['corregimiento_id']
        dates = {'message':'Success'}
        return JsonResponse(dates)


    def put(self,request,id):
        jd = json.loads(request.body)
        zones =list(Zone.objects.filter(id=id).values())
        if len(zones)>0:
           zones = Zone.objects.get(id = id)
           zones.description=jd['description']
           zones.corregimiento_id=jd['corregimeinto_id']
           zones.save()
           dates ={'message':'Success'}
            
        else:
            dates = {'message':'Corregimiento not found...'}
        return JsonResponse(dates)

    def delete(self,request,id):
        zones =list(Zone.objects.filter(id=id).values())
        if len(zones)>0:
            Zone.objects.filter(id=id).delete()
            dates ={'message':'Success'}
        else:
            dates = {'message':'zones not found...'}
        return JsonResponse(dates)