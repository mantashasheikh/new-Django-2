from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Student
from django.http import JsonResponse,HttpResponse
from django.forms.models import model_to_dict

# Create your views here.
@csrf_exempt
def stu_list(req):
    if req.method=="POST":
        # print("Request get from thunder client....")
        j_data = req.body
        # print(data)
        # print(type(data))
        p_data = json.loads(j_data)
        print(p_data)
        print(type(p_data))
        name = p_data.get('stu_name')
        email = p_data.get('stu_email')
        city = p_data.get('stu_city')
        add = p_data.get('stu_add')

        user_data = Student.objects.filter(stu_email=email)
        if user_data:
            p_data = {'msg':'Email Already exist'}
            # j_data = json.dumps(p_data)
            return JsonResponse(p_data)
        else:
            Student.objects.create(stu_name=name,stu_email=email,stu_city=city,stu_add=add)
            p_data = {'msg':'New object created'}
            j_data = json.dumps(p_data)
            return HttpResponse(j_data)
    else:
        all_stu = Student.objects.all()
        # print(list(all_stu.values()))
        # print(all_stu.values_list())
        p_data = list(all_stu.values())
        # return JsonResponse(p_data) # TypeError: In order to allow non-dict objects to be serialized set the safe parameter to False.
        return JsonResponse(p_data,safe=False)

@csrf_exempt
def stu_detail(req,pk):
    db_data =Student.objects.filter(id=pk)
    if db_data:
        if req.method=="PUT":
            j_data = req.body
            p_data = json.loads(j_data)
            name = p_data.get('stu_name')
            email = p_data.get('stu_email')
            city = p_data.get('stu_city')
            add = p_data.get('stu_add')
            if name is not None and email is not None and city is not None and add is not None:
                old_data = Student.objects.get(id=pk)
                old_data.stu_name = name
                old_data.stu_email = email
                old_data.stu_city = city
                old_data.stu_add = add
                old_data.save()
                p_data = {'msg':'Object Updated'}
                return JsonResponse(p_data)
            else:
                d ={'stu_name':name,'stu_email':email,'stu_city':city,'stu_add':add}
                d1={}
                for i in d:
                    if d[i] is None:
                        d1[i]="Field required"
                j_data = json.dumps(d1)
                return HttpResponse(j_data)
            
        elif req.method=='PATCH':
            j_data = req.body
            p_data = json.loads(j_data)
            name = p_data.get('stu_name')
            email = p_data.get('stu_email')
            city = p_data.get('stu_city')
            add = p_data.get('stu_add')
            old_data = Student.objects.get(id=pk)
            if name is not None:
                old_data.stu_name=name
            if email is not None:
                old_data.stu_email=email
            if city is not None:
                old_data.stu_city=city
            if add is not None:
                old_data.stu_add=add
            old_data.save()
            p_data = {'msg':'Object Partially Updated'}
            return JsonResponse(p_data)

        elif req.method=='DELETE':
            old_data = Student.objects.get(id=pk)
            old_data.delete()
            p_data = {'msg':'Object Deleted'}
            return JsonResponse(p_data)

        else:
            stu_data = Student.objects.get(id=pk)
            p_data = model_to_dict(stu_data)
            return JsonResponse(p_data)

    else:
        p_data = {'msg':f'given id {pk} not found in our DB'}
        return JsonResponse(p_data)