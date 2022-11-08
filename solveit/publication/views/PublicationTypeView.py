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
                dates = {'message':'Success','publicationType': publicationType}
            else:
                dates = {'message':'publicationType not found...'}
            return JsonResponse(dates)
        
    def post(self,request):
        jd = json.loads(request.body)
        Publication_Type.objects.create(description=jd['description'])
        dates = {'message':'Success'}
        return JsonResponse(dates)


    def put(self,request,id):
        jd = json.loads(request.body)
        publicationType =list(Publication_Type.objects.filter(id=id).values())
        if len(publicationType)>0:
           publicationType = Publication_Type.objects.get(id = id)
           publicationType.description=jd['description']
           publicationType.save()
           dates ={'message':'Success'}
            
        else:
            dates = {'message':'Corregimiento not found...'}
        return JsonResponse(dates)

    def delete(self,request,id):
        publicationType =list(Publication_Type.objects.filter(id=id).values())
        if len(publicationType)>0:
            Publication_Type.objects.filter(id=id).delete()
            dates ={'message':'Success'}
        else:
            dates = {'message':'publicationType not found...'}
        return JsonResponse(dates)