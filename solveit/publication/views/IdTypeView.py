from django.views import View
from ..models import Id_Type
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

class IdTypeView:
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request,id = 0):
        if(id>0):
            idType = list(Id_Type.objects.filter(id=id).values())
            if len(idType) >0:
                dates = {'message':'Success','idType': idType}
            else:
                dates = {'message':'idType not found...'}
            return JsonResponse(dates)
        else:
            idType = list(Id_Type.objects.values())
            if len(idType)>0:
                dates = {'message':'Success','idType': idType}
            else:
                dates = {'message':'idType not found...'}
            return JsonResponse(dates)
        
    def post(self,request):
        jd = json.loads(request.body)
        Id_Type.objects.create(description=jd['description'])
        dates = {'message':'Success'}
        return JsonResponse(dates)


    def put(self,request,id):
        jd = json.loads(request.body)
        idType =list(Id_Type.objects.filter(id=id).values())
        if len(idType)>0:
            idType = Id_Type.objects.get(id = id)
            idType.description=jd['description']
            idType.save()
            dates ={'message':'Success'}
            
        else:
            dates = {'message':'idType not found...'}
        return JsonResponse(dates)

    def delete(self,request,id):
        idType =list(Id_Type.objects.filter(id=id).values())
        if len(idType)>0:
            Id_Type.objects.filter(id=id).delete()
            dates ={'message':'Success'}
        else:
            dates = {'message':'idType not found...'}
        return JsonResponse(dates)
    
    