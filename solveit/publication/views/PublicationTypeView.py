from django.views import View
from ..models import Publication_Type
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

class PublicationTypeView:
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request,id = 0):
        if(id>0):
            publicationType= list(Publication_Type.objects.filter(id=id).values())
            if len(publicationType) >0:
                dates = {'message':'Success','publicationType': publicationType}
            else:
                dates = {'message':'publicationType not found...'}
            return JsonResponse(dates)
        else:
            publicationType = list(Publication_Type.objects.values())
            if len(publicationType)>0:
                dates = {'message':'Success','zones': publicationType}
            else:
                dates = {'message':'zones not found...'}
            return JsonResponse(dates)
        
    def post(self,request):
        jd = json.loads(request.body)
        Publication_Type.objects.create(description=jd['description'],corregimiento=jd['corregimiento_id'])
        corregimeinto_id_id= jd['corregimiento_id']
        dates = {'message':'Success'}
        return JsonResponse(dates)


    def put(self,request,id):
        jd = json.loads(request.body)
        zones =list(Publication_Type.objects.filter(id=id).values())
        if len(zones)>0:
           zones = Publication_Type.objects.get(id = id)
           zones.description=jd['description']
           zones.corregimiento_id=jd['corregimeinto_id']
           zones.save()
           dates ={'message':'Success'}
            
        else:
            dates = {'message':'Corregimiento not found...'}
        return JsonResponse(dates)

    def delete(self,request,id):
        zones =list(Publication_Type.objects.filter(id=id).values())
        if len(zones)>0:
            Publication_Type.objects.filter(id=id).delete()
            dates ={'message':'Success'}
        else:
            dates = {'message':'zones not found...'}
        return JsonResponse(dates)