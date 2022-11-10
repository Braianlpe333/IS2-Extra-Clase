from django.views import View
from ..models import User
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json


class UserView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request,id = 0):
        if(id>0):
            users = list(User.objects.filter(id=id).values())
            if len(users) >0:
                dates = {'message':'Success','users': users}
            else:
                dates = {'message':'Users not found...'}
            return JsonResponse(dates)
        else:
            users = list(User.objects.values())
            if len(users)>0:
                dates = {'message':'Success','users': users}
            else:
                dates = {'message':'users not found...'}
            return JsonResponse(dates)
        
    def post(self,request):
        jd = json.loads(request.body)
        if(self.valitades(jd)):
            User.objects.create(zone_id_id=jd['zone_id_id'],idType_id_id=jd['idType_id_id'],name=jd['name'],lastname=jd['lastname'],
            description=jd['description'],idnumber=jd['idnumber'],phone=jd['phone'],mail=jd['mail'],password=jd['password'])
            dates = {'message':'Success'}
        else:
            dates = {'message':'Error try to create a new user'}
        return JsonResponse(dates)


    def put(self,request,id):
        jd = json.loads(request.body)
        users =list(User.objects.filter(id=id).values())
        if len(users)>0:
            users = User.objects.get(id = id)
            users.description=jd['description']
            users.save()
            dates ={'message':'Success'}
            
        else:
            dates = {'message':'users not found...'}
        return JsonResponse(dates)

    def delete(self,request,id):
        users =list(User.objects.filter(id=id).values())
        if len(users)>0:
            User.objects.filter(id=id).delete()
            dates ={'message':'Success'}
        else:
            dates = {'message':'users not found...'}
        return JsonResponse(dates)

    def valitades(self,jd):
        idnumber = list(User.objects.filter(idnumber=jd["idnumber"]).values())
        idtype = list(User.objects.filter(idType_id=jd["idType_id_id"]).values())
        if(len(idnumber)>0 and len(idtype)>0):
            return False
        else:
            return True
        