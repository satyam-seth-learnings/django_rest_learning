from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse

# Create your views here.

# Model Object - Single Student Data
# def student_detail(request):
#     # stu=Student.objects.get(id=1)
#     stu=Student.objects.get(id=2)
#     print(stu)
#     serializer=StudentSerializers(stu)
#     print(serializer)
#     print(serializer.data)
#     json_data=JSONRenderer().render(serializer.data)
#     print(json_data)
#     return HttpResponse(json_data,content_type='application/json')

def student_detail(request,pk):
    stu=Student.objects.get(id=pk)
    serializer=StudentSerializers(stu)
    # json_data=JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data,content_type='application/json')
    return JsonResponse(serializer.data)

#  Query Set - All Student Data
def student_list(request):
    stu=Student.objects.all()
    serializer=StudentSerializers(stu,many=True)
    # json_data=JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data,content_type='application/json')
    return JsonResponse(serializer.data,safe=False)