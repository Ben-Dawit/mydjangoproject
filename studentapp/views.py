from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import HttpResponse, JsonResponse

from studentapp.models import Students
from studentapp.serializers import studentSerializer

def home(request):
    context = {
        'Students': Students.objects.all() 
    }
    return render(request, 'studentapp/home.html',context)

@csrf_exempt
def studentApi(request, id=0):
    
    if request.method == 'GET' :
        # logic for the get method, gets a list of all the students
        students = Students.objects.all()
        student_serializer = studentSerializer(students, many = True)
        return JsonResponse(student_serializer.data, safe=False)
        
    elif request.method == 'POST' :
        #logic for post method, enter info like this
        #{"StudentId": 0, "StudentGrade": 85}
        #you should get "Added Successfully" or "Failed to Add"
        students_data = JSONParser().parse(request)
        student_serializer = studentSerializer(data = students_data)
        if student_serializer.is_valid():
            student_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe = False)
    
# to start the server run 'python manage.py runserver' 
# Create your views here.
