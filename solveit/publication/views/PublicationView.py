from django.views import View
from ..models import Publication
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

class PublicationView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request,id = 0):
        if(id>0):
            publications = list(Publication.objects.filter(id=id).values())
            if len(publications) >0:
                dates = {'message':'Success','Publication': publications}
            else:
                dates = {'message':'Publication not found...'}
            return JsonResponse(publications)
        else:
            publications = list(Publication.objects.values())
            if len(publications)>0:
                dates = {'message':'Success','Publications': publications}
            else:
                dates = {'message':'Publications not found...'}
            return JsonResponse(dates)
        
    def post(self,request):
        jd = json.loads(request.body)
        try:
            Publication.objects.create(title=jd['title'],description=jd['description'],phone=jd['phone'],
            publication_type_id_id=jd['publication_type_id'],user_id_id=jd['user_id'],zone_id_id=jd['zone_id'])
            dates = {'message':'Success'}
        except ValueError:
                dates ={'message':ValueError}
        return JsonResponse(dates)


    def put(self,request,id):
        jd = json.loads(request.body)
        publications =list(Publication.objects.filter(id=id).values())
        if len(publications)>0:

            try:
                publications = Publication.objects.get(id = id)
                publications.title=jd['title']
                publications.description=jd['description']
                publications.phone=jd['phone']
                publications.publication_type_id_id=jd['publication_type_id']
                publications.user_id_id=jd['user_id']
                publications.zone_id_id=jd['zone_id']
                publications.save()
                dates ={'message':'Success'}
            except ValueError:
                dates ={'message':ValueError}
            
        else:
            dates = {'message':'City not found...'}
        return JsonResponse(dates)

    def delete(self,request,id):
        citys =list(Publication.objects.filter(id=id).values())
        if len(citys)>0:
            Publication.objects.filter(id=id).delete()
            dates ={'message':'Success'}
        else:
            dates = {'message':'City not found...'}
        return JsonResponse(dates)